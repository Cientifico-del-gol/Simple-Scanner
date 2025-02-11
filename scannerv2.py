import csv
import os
import tkinter as tk

def scan():
    convlist=list()
    unique_exes=set()

    log_message('Reading and parsing .csv database...')

    with open('full.csv', mode='r',  encoding='utf-8') as file:
        csvfh = csv.DictReader(file, fieldnames=['F'])
        for row in csvfh:
            exe_position = row['F'].find('.exe')
            data = row['F'][:exe_position + 4]
            if exe_position==-1:
                continue
            else:
                convlist.append(data)
    
        for line in convlist:
            exe=line.rsplit('"',1)[-1].strip()
            unique_exes.add(exe)

    log_message('Threat names identified!')

#print('Extracting them in a txt file...')

    convlist2=list(unique_exes)
#with open('newlistmalware.txt', 'w', encoding='utf-8') as output_file:
    #output_file.write(",".join(convlist2))

#print('Results extracted to newlistmalware.txt')

    path='C:/'
    pathfinder=os.fsencode(path)

    log_message('Scanning computer...')

    exelist=list()
    for dirpath, dirnames, filenames in os.walk(path):
        for fname in filenames:
            if fname.endswith('.exe'):
                exelist.append(fname)

    log_message('Comparing results to known malware database...')

    threatlist=set()
    for line in convlist2:
        for item in exelist:
            if item in line:
                threatlist.add(item)
                #count+=1

    count=len(threatlist)
    log_message(f'Possible threats found: {count}')

    log_message('Printing possible threats in a txt file!')

    with open('Possiblethreats.txt', 'w', encoding='utf-8') as lst:
        lst.write(f'Total possible threats:{count}\n')
        for exe in threatlist:
            lst.write(exe+'\n')
    #lst.write('\n'.join(threatlist))

    log_message('Possible threats txt printed!')
    log_message('All done!')

def log_message(message):
    log_text.insert(tk.END, message+'\n')
    log_text.see(tk.END)

if __name__=='__main__':
    # Create a tkinter window
    root=tk.Tk()
    root.title('Windows Endpoint Malware Scanner')
    root.geometry('800x400')
    root.config(bg='black')

    # Output field using Entry
    #log=tk.Entry(root,font=('consolas',12),justify='center',)
    #log.config(bg='black',fg='green',state='readonly')
    #log.pack(pady=(50,10),padx=30,fill='x')
    
    # Create a button to scan
    button=tk.Button(root,text='Begin scanning',padx=5,pady=5,font=('consolas',12),command=scan,
                     bg='black',fg='green',highlightbackground='green',highlightcolor='green')
    button.pack(pady=(20,10))

    log_text=tk.Text(root,font=('consolas',12),bg='black',fg='green',
                     highlightbackground='green',highlightcolor='green')
    log_text.pack(pady=(50,10),padx=30,fill='x') 
    
    # Loop the tkinter window
    root.mainloop()
