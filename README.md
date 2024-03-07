This is a simple Python program designed to scan your computer for .exe files, which are one of the most common sources of malware, and compare the results to a database of known malware extracted from "https://bazaar.abuse.ch/" on 03/02/2024. That way, you can identify the potentially dangerous .exe files inside your device. However, in many cases, lagitimate files are treated as possible threats since they behave similarly to malware and deliquents tend to disguise their malware as those legitimate files. To investigate if they are actually safe and legitimate:

1. Got to C:\ in your file explorer
2. Type in the searchbar the name of the .exe file (It may take a bit)
3. When found, check it's digital signature by right clicking them and searching for it in "properties". 

If you see that there is no signature or that it has a strange name you should probably delete the file, BUT DO BE EXTREMELY CAUTIOUS SINCE YOU CAN ACCIDENTALY DELETE ESSENTIAL PROGRAMS FORM YOUR DEVICE. SO, BEFORE DELETING ANYTHING, YOU SHOULD GOOGLE THE NAMES OF THE FILES AND SIGNATURES TO INVESTIGATE IF THEY ARE FROM MALICIOUS ACTORS OR NOT.

Also, due to the everchanging nature of digital threats, the database on that internet site is constantly being updated (aprox. once every hour), so the data might be a bit out of date. However, there is a way to update the database and get an updated scan:

1. Go to https://bazaar.abuse.ch/export/
2. Export most recent .csv file
3. Put .csv file in the "materials" folder
4. Run the file "fullread.py" in that same folder to parse the database and extract the .exe files in the document, using the terminal form your device (assuming you have also downloaded Python in your computer)
5. It should produce or update a txt document with a list of the .exe threats identified in the .csv file inside that same folder
6. Copy or move the txt file to the folder "ScannerDownLoad"
7. Run the file "scannermalware" inside that folder using the terminal form your device
8. It should produce or update (if you have already run the scanner) a txt document called "Possiblethreats.txt" with the list of suspicious .exe programs

IMPORTANT: This is not an "antivirus" and it doesn't replace their use or the use of a VPN or not taking the necessary precautions to secure your device!

Ret'urcye mhi, vod!
-El Científico del Gol
