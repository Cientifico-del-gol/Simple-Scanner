import csv

convlist=list()
unique_exes=set()

Print('Reading and parsing .csv database...')

with open('full.csv', mode='r',  encoding='utf-8') as file:
    csvfh = csv.DictReader(file, fieldnames=['A'])
    for row in csvfh:
        exe_position = row['A'].find('.exe')
        data = row['A'][:exe_position + 4]
        if exe_position==-1:
            continue
        else:
            convlist.append(data)
    
    for line in convlist:
        exe=line.rsplit('"',1)[-1].strip()
        unique_exes.add(exe)

print('Threat names identified!')

print('Extracting them in a txt file...')

convlist2=list(unique_exes)
with open('newlistmalware.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(",".join(convlist2))

print('Results extracted to newlistmalware.txt')

print('All done!')

print('Remeber to copy or move txt file to ScannerDownLoad folder before running scannermalware.py!')