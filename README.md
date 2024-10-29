This was my first coding project, and is a basic file-based ‘malware scanner’. The idea is to automate a very simple scanner for Windows Operating systems using Python. In short, the algorith reads a list of known malware names (specifically ‘.exe’ files) from a ‘.csv’ file, compiles these into a malware signature list, and scans the local computer’s file system for matching ‘.exe’ files. Any matches are flagged as potential threats and logged in an output ‘.txt’ file. To run the algorithm in devices that do not have Python installed, I created an ‘.exe’ file using PyInstaller that is also stored at it’s GitHub repository.

I am aware that this is a very basic algorithm with many shortcomings, such as:

The unreliability of using file names to detect malware. Furthermore, not every malware is a ‘.exe’ file, as even fileless malware exists.

The amount of false positives derived from ‘.exe’ malicious files trying to masquarade as legitimate files.

The lack of independance from the ‘.csv’ database.

In the future I plan to address each point by either transforming this simple Python code into a Deep Learning model that can “learn” to identify more malware characteristics to predict very accurately if the scanned files of all types are possible malware; even if there is no database present, as the model would already trained and ready to deploy.

To investigate if they are actually safe and legitimate:

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
