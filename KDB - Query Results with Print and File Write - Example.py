import #FileCreatedWithHashName# Import the file that you created that contains the hash version of credential
import base64 #Import the base64 library that will be used to decrpyt the hash to establish a connection
import cx_Oracle #Import library used for an oracle connection

v_user = input( "Enter user : " ) #Prompt the user to enter the credential
v_pass = base64.b64decode(#FileCreatedWithHashName#.password_crypt)
v_instance = #"DatabaseInstance"#

ConnectToDB = cx_Oracle.connect(v_user,v_pass,v_instance)

print('\n'+'Connected established with Oracle Version: ' + ConnectToDB.version) #Prints the version of the OracleClient you are using
print('Connected to ' + v_instance + ' as user ' + v_user) #Prints the Database you are connected to along with which user using created variables


ConnectToDB = cx_Oracle.connect(v_user,v_pass,v_instance)

print('\n'+'Connected established with Oracle Version: ' + ConnectToDB.version)
print('Connected to ' + v_instance + ' as user ' + v_user)

sql_query = """

select trunc(sysdate-1) as listed_date, 'Yesterday' as listed_day
from dual

--select trunc(sysdate) as listed_date, 'Today' as listed_day
--from dual

--select trunc(sysdate+1) as listed_date, 'Tomorrow' as listed_day
--from dual

"""


# Run your query, the result is stored as `data`
curs = ConnectToDB.cursor()
curs.execute(sql_query)
data = curs.fetchall()

# Create the csv file
# a+ creates the file if it doesn't exist and then will append the data

AppendFile = open(v_CompleteFileName,"a+", newline='')
writer = csv.writer(AppendFile)
# Add the header/column names
#Header = ["Date","Day"]
#writer.writerow(Header)

# Iterate over `data`  and  print to screen
for row in data:
    print("\n"+str(row))

# Iterate over `data`  and  write to the csv file
for row in data:
    writer.writerow(row)