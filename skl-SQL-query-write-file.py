#===============================================================================
# Export Oracle database tables to CSV files
#--------------------------------------------------------------------------
#
# how to connect to Oracle, run a query, access the query metadata, 
# process the query results by row or by column, write to normal text 
# files, create CSV files
#
#--------------------------------------------------------------------------
# (2018-02-27) - sklyon 
#===============================================================================

import getpass
import cx_Oracle
import csv

#=======================================
#  Define or prompt for authentication
#---------------------------------------

v_usr = input( "Enter user : " )
v_pwd = getpass.getpass( prompt="Enter pwrd : " )

v_cnct = v_usr + " / " + v_pwd + " @ edw"



#=======================================
#  Define the query
#---------------------------------------

v_Query1 = """\
   ---
   select  Empno  as "ID"
        ,  initcap(ename)  as "Who"
        ,  lower(job)  as "What"
        ,  mgr  as mgr_id
        ,  to_char(hiredate,'YYYY-Mon-DD') as "Hired-On"
        ,  sal
        ,  deptno
     from  train.emp
    where  job in ( 'ANALYST', 'SALESMAN', 'CLERK' )
   --- """

v_Query2 = """ select to_char(sysdate,'YYYY-Mon-DD (Dy) HH24:MI:SS') as "DateTime" from dual """


#===================================================================================================
print( "\n"+80*"="+"\n"+6*"="+" Start of Output "+6*"="+"   "+7*"\*/   "+6*"="+"\n"+80*"="+"\n" )
#===================================================================================================



#=======================================
#  Run Query - Output time
#---------------------------------------

v_Qrslt1 = cx_Oracle.connect(v_cnct).cursor().execute( v_Query2 )

print()

for v_result_row in v_Qrslt1:
   print( "=====> Date-Time is: ( " + v_result_row[0] + " )" )

print()



#=======================================
#  Save query results in a file
#    row by row
#---------------------------------------

v_Qrslt1 = cx_Oracle.connect(v_cnct).cursor().execute( v_Query2 )

v_out_file_text = open("Results1-DTS.txt", "w")

for v_result_row in v_Qrslt1:
   v_out_file_text.write( "DTS: " + v_result_row[0] + "\n" )

v_out_file_text.close()

print("=====> DTS saved in file !")
print()



#=======================================
#  output query metadata
#    connect and run query in steps
#    show the metadata for the query
#---------------------------------------

v_session = cx_Oracle.connect(v_cnct)
v_cursor = v_session.cursor()
v_Qrslt2 = v_cursor.execute(v_Query1)

print("=====> Column Metadata Follows:")
print()

for v_column_metadata in v_Qrslt2.description:
   print(v_column_metadata)

print()



#=======================================
#  write query results to simple file
#    uses query results from
#    previous query: v_qRslt2
#    column by column
#---------------------------------------

v_out_file_text = open("Results2.txt", "w")

for v_result_row in v_Qrslt2:
   for v_next_column in v_result_row:
      v_out_file_text.write( str(v_next_column) + "   |   " )
   v_out_file_text.write("\n")

v_out_file_text.close()

print("=====> Text file created !")
print()



#=======================================
#  Run query and dump to CSV file
#    row by row
#---------------------------------------

v_Qrslt3 = cx_Oracle.connect(v_cnct).cursor().execute( v_Query1 )

v_outFile = open( "Results3.csv",'w', newline='' )
v_out = csv.writer( v_outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL )

v_include_column_header_row = True

if v_include_column_header_row:
   v_column_header_row = []
   for v_col_hdr in v_Qrslt3.description:
      v_column_header_row.append(v_col_hdr[0])
   v_out.writerow(v_column_header_row)

for v_result_row in v_Qrslt3:
   v_out.writerow(v_result_row)

v_outFile.close()

print("=====> CSV file created !")
print()



#=======================================
#  Print out CSV-type records
#    column by column for each row
#---------------------------------------

print("=====> CSV-Type results: ")
print()

v_Qrslt4 = cx_Oracle.connect(v_cnct).cursor().execute( v_Query1 )

v_col_cnt = len(v_Qrslt4.description)
for i in range( v_col_cnt ):
   if i < v_col_cnt-1:  print( v_Qrslt4.description[i][0], end=', ' )
   else:                print( v_Qrslt4.description[i][0] )

print("--------------------------------------------------------------------")

for v_row in v_Qrslt4:
   v_col_cnt = len( v_row )
   for i in range( v_col_cnt ):
      if i < (v_col_cnt - 1):  print( '"'+str(v_row[i])+'"', end=', ' )
      else:                    print( '"'+str(v_row[i])+'"' )



#===================================================================================================
print( "\n"+80*"="+"\n"+6*"="+" Start of Output "+6*"="+"   "+7*"\*/   "+6*"="+"\n"+80*"="+"\n" )
#===================================================================================================


#===============================================================================
# Eof
#===============================================================================
