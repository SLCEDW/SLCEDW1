import csv
import os

## Constants defined for file operations
READ = "r"
READWRITE = "w+"
WRITE = "w"
APPEND = "a"
BINARY = "b"

#Where you are going to read the file from and where you are going to write the file too
v_FilePath = #Specify your file will be placed

v_FileName = #Name of your file being read
v_NewFileName = #Name of your file being created and written to

#Use the OS package to create your file paths of the files being read and created for writing
v_ReadFileName = os.path.join(v_FilePath,v_FileName+".csv")
v_WriteFileName = os.path.join(v_FilePath,v_NewFileName+".csv")

#Files you are going open for reading and writing
with open(v_WriteFileName, READWRITE, newline='') as WriteFile, open(v_ReadFileName,READ) as ReadFile:
    #Variable for the reader file
    reader = csv.DictReader(ReadFile,delimiter=',')
    #Variable for the writer file
    writer = csv.writer(WriteFile,delimiter='|')
    header = [#Column1,#Column2]
    #Print out or write the header of your file
        #print(header)
        #writer.writerow(header)
    #Loop through the records of the file being read
    for row in reader:
    #Specify if you want to print the items to the screen or write them to the written file opened
        #print(row)
        #print(row['Record_ID'],row['Patient_ZIP'])
        #WriteFile.write(str(row['Column1']+"|"+row['Column2']+"\r\n"))