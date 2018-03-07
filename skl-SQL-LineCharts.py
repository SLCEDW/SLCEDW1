#===============================================================================
# SQL Query then Plot the Results in a Line Chart (multiple series)
#--------------------------------------------------------------------------
#
# Thanks to Stanley C for figguring out how to do matplotlib charts!
#
#--------------------------------------------------------------------------
# (2018-03-07) - sklyon 
#===============================================================================

import cx_Oracle
import matplotlib.pyplot  as xMp
import matplotlib.dates   as xMd





########################################
# Build the Oracle Connect String
#=======================================
import getpass
#-----
vUsr = input( ">>> Enter UserName : " )
vPwd = getpass.getpass( prompt = ">>> Enter Password : " )
vDbs = input( ">>> Enter Database : " )
#---------------------------------------

vCnctStr = vUsr + " / " + vPwd + " @ " + vDbs





########################################
# Connect to Database
#=======================================

vOraSession = cx_Oracle.connect( vCnctStr )





########################################
# Define and Run the Query
#=======================================

vQry = """\
   ------------
   with
     w_data  as
       ( select  NULL  as grp
              ,  NULL  as dts
              ,  NULL  as m
           from  dual  where 1=2
         -----
         union all select  'alpha',  sysdate-20,  12  from dual
         union all select  'alpha',  sysdate-19,  15  from dual
         union all select  'alpha',  sysdate-18,  25  from dual
         union all select  'alpha',  sysdate-17,  56  from dual
         union all select  'alpha',  sysdate-15,  42  from dual
         union all select  'alpha',  sysdate-14,  11  from dual
         union all select  'alpha',  sysdate-13,  05  from dual
         union all select  'alpha',  sysdate-12,  02  from dual
         -----
         union all select  'BUZRD',  sysdate-20,  72  from dual
         union all select  'BUZRD',  sysdate-19,  68  from dual
         union all select  'BUZRD',  sysdate-18,  66  from dual
         union all select  'BUZRD',  sysdate-17,  51  from dual
         union all select  'BUZRD',  sysdate-15,  48  from dual
         union all select  'BUZRD',  sysdate-14,  49  from dual
         union all select  'BUZRD',  sysdate-13,  45  from dual
         union all select  'BUZRD',  sysdate-12,  35  from dual
         union all select  'BUZRD',  sysdate-11,  38  from dual
         union all select  'BUZRD',  sysdate-10,  41  from dual
         union all select  'BUZRD',  sysdate-09,  44  from dual
         -----
         union all select  'crank',  sysdate-20,  09  from dual
         union all select  'crank',  sysdate-19,  18  from dual
         union all select  'crank',  sysdate-18,  29  from dual
         union all select  'crank',  sysdate-17,  37  from dual
         union all select  'crank',  sysdate-15,  45  from dual
         union all select  'crank',  sysdate-14,  56  from dual
         union all select  'crank',  sysdate-13,  62  from dual
         union all select  'crank',  sysdate-12,  70  from dual
       )
   select  grp                  -- 0 -
        ,  trunc(dts) as dts    -- 1 -
        ,  m                    -- 2 -
     from  w_data
    order  by  1, 2
   ------------ """

vQryRslt = vOraSession.cursor().execute( vQry )





########################################
# Put the Query Results into
# nested Lists
#=======================================

vQdata, vLastVal, vi = [], "-na-", 0

for vRow in vQryRslt:
   if (vLastVal != vRow[0]):   # new group
      vQdata.append([vRow[0],[],[]])
      vLastVal = vRow[0]
      vi += 1
   vQdata[vi-1][1].append(vRow[1])
   vQdata[vi-1][2].append(vRow[2])








########################################
# Show data (unpack the nested lists).
# Would been simpler to print out the
# query data before it was packed.
#=======================================

print( "\n" + "Showing all Data:" + "\n" )

for vi in range(len(vQdata)):
  for vj in range(len(vQdata[vi][1])):
    print( "   >> Grp= {0:6}   DTS= {1:19}   Val={2:>3}".format
           ( vQdata[vi][0]
           , str(vQdata[vi][1][vj])
           , str(vQdata[vi][2][vj])
         ) )
print()





########################################
# Plot the data
#=======================================

for vi in range( len(vQdata) ):
  xMp.plot( vQdata[vi][1], vQdata[vi][2], ".-", label = vQdata[vi][0], lw = 1 )

xMp.xlabel( "Date" ); xMp.ylabel( "Measure" )
xMp.legend ( loc = "center left", bbox_to_anchor = ( 1, 0.5 ) )
xMp.title( "Charting Multiple Data Series Results from a Query" )
xMp.gca().xaxis.set_major_formatter( xMd.DateFormatter( '%b\n%d' ) )
xMp.show()



#-------------------------------------------------------------------------------
