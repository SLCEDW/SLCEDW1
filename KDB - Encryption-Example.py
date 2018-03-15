import base64 #Importing the library used to encrypt items
import os.path #Importing the library for the functions used to create file paths#

FilePath = #'FilePath' Place the folder location for which you want to write your file#
FileName = 'PasswordEncryption' #Name of the file you are creating#
#FileName = 'PasswordEncryptionDefault' Demo File
CompleteFileName = os.path.join(FilePath,FileName+".txt") #Function used to create the file location path and name with type#

password = #'PlacePasswordHere'#
password_crypt = base64.b64encode(password.encode()) #Function that is used to encrypt password above and creats a hash of password#


passwordFile = open(CompleteFileName,"wb") #Process to create the txt file that stored the encryption of the password
toFile = password_crypt
passwordFile.write(toFile)
passwordFile.close()
