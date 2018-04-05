#===============================================================================
# Display Query Data in a Table
#--------------------------------------------------------------------------
# (2018-04-05) - sklyon
#===============================================================================

import getpass
import cx_Oracle
from tkinter import *
from tkinter import ttk



########################################
# Some Global variables
#=======================================
vHeader, vCell = [], []
vRows, vCols   = 0, 0



########################################
# Build the Oracle Connect String
#=======================================
import getpass
#-----
vUsr = input( ">>> Enter UserName : " )
vPwd = getpass.getpass( prompt = ">>> Enter Password : " )
vDbs = input( ">>> Enter Database : " )
#=======================================
vCnctStr = vUsr + "/" + vPwd + "@" + vDbs






########################################
# Define functions for buttons
#=======================================
def vClick_Left():                          # Shift Data in Cells: Left
  global vRows, vCols, vCell, vHeader
  for v1 in range( vRows ):
    vTmp = vCell[v1][0].get()
    vP = [ vTmp, "" ]
    for v2 in range( vCols-1, -1, -1 ):
      vP[1] = vP[0]
      vP[0] = vCell[v1][v2].get()
      vCell[v1][v2].delete(0, 'end')
      vCell[v1][v2].insert(0, vP[1])
  vTmp = vHeader[0].get()
  vP = [ vTmp, "" ]
  for v2 in range( vCols-1, -1, -1 ):
    vP[1] = vP[0]
    vP[0] = vHeader[v2].get()
    vHeader[v2].delete(0, 'end')
    vHeader[v2].insert(0, vP[1])
#------------
def vClick_Right():                         # Shift Data in Cells: Right
  global vRows, vCols, vCell, vHeader
  for v1 in range( vRows ):
    vTmp = vCell[v1][vCols-1].get()
    vP = [ vTmp, "" ]
    for v2 in range( vCols ):
      vP[1] = vP[0]
      vP[0] = vCell[v1][v2].get()
      vCell[v1][v2].delete(0, 'end')
      vCell[v1][v2].insert(0, vP[1])
  vTmp = vHeader[vCols-1].get()
  vP = [ vTmp, "" ]
  for v2 in range( vCols ):
    vP[1] = vP[0]
    vP[0] = vHeader[v2].get()
    vHeader[v2].delete(0, 'end')
    vHeader[v2].insert(0, vP[1])
#------------
def vClick_Up():                            # Shift Data in Cells: Up
  global vRows, vCols, vCell, vHeader
  for v2 in range( vCols ):
    vTmp = vCell[0][v2].get()
    vP = [ vTmp, "" ]
    for v1 in range( vRows-1, -1, -1 ):
      vP[1] = vP[0]
      vP[0] = vCell[v1][v2].get()
      vCell[v1][v2].delete(0, 'end')
      vCell[v1][v2].insert(0, vP[1])
#------------
def vClick_Down():                          # Shift Data in Cells: Down
  global vRows, vCols, vCell, vHeader
  for v2 in range( vCols ):
    vTmp = vCell[vRows-1][v2].get()
    vP = [ vTmp, "" ]
    for v1 in range( vRows ):
      vP[1] = vP[0]
      vP[0] = vCell[v1][v2].get()
      vCell[v1][v2].delete(0, 'end')
      vCell[v1][v2].insert(0, vP[1])
#------------







########################################
# Connect to Database and run query.
#=======================================
vOraSession = cx_Oracle.connect( vCnctStr )
###
vQry = """\
------
select  case
          when  Empno = 7902  then '@@ 7902 @@'
          else  to_char( Empno )
        end  as "ID"
     ,  case
          when  initcap(ename) = 'Ford'  then '@@ Ford @@'
          else  initcap(ename)
        end  as "Who"
     ,  lower(job)  as "What"
     ,  mgr  as mgr_id
     ,  to_char(hiredate,'YYYY-Mon-DD') as "Hired-On"
     ,  sal
     ,  deptno
     ,  to_char(sysdate, 'Mon-DD HH24:MI:SS') as "TimeStamp"
  from  train.emp
 where  1=1
   and  job in ( 'ANALYST', 'SALESMAN', 'CLERK' )
   and  rownum < 50
 order  by ename
------ 
"""
###
vQryRslt = vOraSession.cursor().execute( vQry )
#########





#=======================================
#  Store the query-results in lists
#---------------------------------------
vQryHdr, vQryData = [], []
###
v_col_cnt = len(vQryRslt.description)
for v2 in range( v_col_cnt ):
   vTmp = vQryRslt.description[v2][0]
   vQryHdr.append( vTmp )
###
v1 = 0
for v_row in vQryRslt:
   vQryData.append([])
   v_col_cnt = len( v_row )
   for v2 in range( v_col_cnt ):
      vTmp = str(v_row[v2])
      vQryData[v1].append(vTmp)
   v1 += 1

vCols = len( vQryData[0] )
vRows = len( vQryData )



#=======================================
#  Build the Frames
#---------------------------------------
vWndo = Tk()
vWndo.title( "Query Results" )
vWndo.geometry( str(100*vCols + 24) + "x" + str(20*vRows + 100) )

# Make a frame to put the buttons in:
vFrm1 = ttk.Frame(vWndo, padding="3 3 3 3")
vFrm1.grid(column=0, row=0)
vFrm1.columnconfigure(0, weight=1)
vFrm1.rowconfigure(0, weight=1)

# Make a frame to put the column-names in:
vFrm2 = ttk.Frame(vWndo, padding="12 12 12 12")
vFrm2.grid(column=0, row=1, sticky=(N, W, E, S))
vFrm2.columnconfigure(0, weight=1)
vFrm2.rowconfigure(0, weight=1)

# Make a frame to put the data-grid in:
vFrm3 = ttk.Frame(vWndo, padding="12 12 12 12")
vFrm3.grid(column=0, row=2, sticky=(N, W, E, S))
vFrm3.columnconfigure(0, weight=1)
vFrm3.rowconfigure(0, weight=1)



#=======================================
#  Create the Buttons
#---------------------------------------
vBtn1 = Button( vFrm1, text = "Left", command = vClick_Left )
vBtn1.grid( column = 0, row = 0 )
###
vBtn2 = Button( vFrm1, text = "Right", command = vClick_Right )
vBtn2.grid( column = 1, row = 0 )
###
vBtn3 = Button( vFrm1, text = "Up", command = vClick_Up )
vBtn3.grid( column = 2, row = 0 )
###
vBtn4 = Button( vFrm1, text = "Down", command = vClick_Down )
vBtn4.grid( column = 3, row = 0 )



#=======================================
#  Put data into the column-name grid
#  and into the data-grid:
#---------------------------------------
for v2 in range( vCols ):
  vTmp = Entry( vFrm2, width = 16 )
  vHeader.append( vTmp )
  vHeader[v2].grid( row = 0, column = v2 )
  vHeader[v2].config( {"background": "Grey"} )
  vHeader[v2].insert( 0, vQryHdr[v2] )
###
for v1 in range( vRows ):
  vCell.append( [] )
  for v2 in range( vCols ):
    vTmp = Entry( vFrm3, width = 16 )
    vCell[v1].append( vTmp )
    vCell[v1][v2].grid( row = v1, column = v2 )
    vCell[v1][v2].insert( 0, vQryData[v1][v2] )




#=======================================
# Display the whole thing and 
# wait for input
#---------------------------------------
vWndo.mainloop()





vNull = input( ">>> Enter to continue : " )
#===============================================================================
# Eof
#===============================================================================
