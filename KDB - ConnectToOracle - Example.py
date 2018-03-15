import #FileCreatedWithHashName# Import the file that you created that contains the hash version of credential
import base64 #Import the base64 library that will be used to decrpyt the hash to establish a connection
import cx_Oracle #Import library used for an oracle connection

v_user = input( "Enter user : " ) #Prompt the user to enter the credential
v_pass = base64.b64decode(#FileCreatedWithHashName#.password_crypt)
v_instance = #"DatabaseInstance"#

ConnectToDB = cx_Oracle.connect(v_user,v_pass,v_instance)

print('\n'+'Connected established with Oracle Version: ' + ConnectToDB.version) #Prints the version of the OracleClient you are using
print('Connected to ' + v_instance + ' as user ' + v_user) #Prints the Database you are connected to along with which user using created variables


#Query to run on the database#
sql_query = """

select trunc(sysdate-1) as date_record
from dual
union
select trunc(sysdate) as date_record
from dual
union
select trunc(sysdate+1) as date_record
from dual

"""

#Results returned by the query are printed to the screen
some_cursor = ConnectToDB.cursor()
results = some_cursor.execute( sql_query )

for row in results:
    print(row[0])
