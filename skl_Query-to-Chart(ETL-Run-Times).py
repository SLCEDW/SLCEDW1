#===============================================================================
# SQL Query - Line Plot
#--------------------------------------------------------------------------
# Pull ETL run times for specified jobs and plot the results
#--------------------------------------------------------------------------
# (2018-04-05) - sklyon
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
#=======================================
vCnctStr = vUsr + "/" + vPwd + "@" + vDbs





########################################
# Connect to Database and run query.
#=======================================
vOraSession = cx_Oracle.connect( vCnctStr )
#----------------------------------
# Query should contain data with 
# these columns:
#   Group-Name, x-Values, y-Values
# The columns names are irrelevant.
# Data can have multiple Groups.
# Data should be sorted by 1, 2
#----------------------------------
vQry = """\
--------------------------------------------------------------------------------
-- Find ETL-ID numbers
--------------------------------------------------------------------------------
--  select  j.data_mart_id,  m.data_mart_name
--       ,  j.etl_id,  j.etl_nm
--       ,  j.active_flg,  j.primary_architect_user_id
--    from  metadata.etl_job   j
--    join  metadata.data_mart m on ( j.data_mart_id = m.data_mart_id )
--   order  by  j.data_mart_id, j.etl_nm ;
--------------------------------------------------------------------------------
with
  w_etl_list  as
    ( select  NULL  as sequence_no
           ,  NULL  as etl_id
           ,  NULL  as short_etl_nm
        from  dual  where 1=2
      union all select   1, 1641, 'MG-PCP'    from dual
      union all select   2, 1224, 'PCP-SCP'   from dual
      union all select   3, 1209, 'HprTnsn'   from dual
      union all select   4,  264, 'CDR-Raw'   from dual
      union all select   5, 9999, 'xxxx'      from dual
    )
select  b.short_etl_nm
     ,  trunc(a.job_begin_dts)  as x_val  /* Run Dt */
     ,  round((a.job_end_dts - a.job_begin_dts)*24*60)  as y_val  /* Runtime in Min */
  from  edw_util.etl_job_run_instance  a
  join  w_etl_list                     b  on ( a.etl_id = b.etl_id )
 where  a.job_end_dts is not NULL
   and  a.job_begin_dts > ( sysdate - 35 )   /* Days Back */
 order  by 1, 2
--------------------------------------------------------------------------------
"""
###
vQryRslt = vOraSession.cursor().execute( vQry )
#########





########################################
# Query Results ===> Nested Lists
#=======================================
# Structure of Nested-List data:
#   vQdata = 
#     [ [ "Grp1", [x1,x2,x3,...], [y1,y2,y3,...] ]
#     , [ "Grp2", [x1,x2,x3,...], [y1,y2,y3,...] ] 
#     , [ "Grp3", [x1,x2,x3,...], [y1,y2,y3,...] ]
#     , ... 
#     ]
#---------------------------------------
vQdata   = []
vLastVal = "~*na*~"
vi       = 0
###
for vRow in vQryRslt:
   if (vLastVal != vRow[0]):
      vQdata.append([vRow[0],[],[]])
      vLastVal = vRow[0]
      vi += 1
   vQdata[vi-1][1].append(vRow[1])
   vQdata[vi-1][2].append(vRow[2])





########################################
# Set-Up Plot Marker-Line Styles
#   OPTIONAL
#=======================================
vLineStyles = \
  [ { "linestyle":"-", "linewidth":1, "color":"#d8d8d8"
    , "marker":".", "markeredgecolor":"#a50000", "markerfacecolor":"#ff87b5" }  # red
  , { "linestyle":"-", "linewidth":1, "color":"#d8d8d8"
    , "marker":".", "markeredgecolor":"#00ba00", "markerfacecolor":"#00ff00" }  # green
  , { "linestyle":"-", "linewidth":1, "color":"#d8d8d8"
    , "marker":".", "markeredgecolor":"#0000ff", "markerfacecolor":"#0091ff" }  # blue
  , { "linestyle":"-", "linewidth":1, "color":"#d8d8d8"
    , "marker":".", "markeredgecolor":"#818100", "markerfacecolor":"#ffff00" }  # yellow
  , { "linestyle":".-", "linewidth":1 } 
  , { "linestyle":".-", "linewidth":1 }  
  , { "linestyle":".-", "linewidth":1 }  
  , { "linestyle":".-", "linewidth":1 }  
  , { "linestyle":".-", "linewidth":1 }  
  , { "linestyle":".-", "linewidth":1 }  
  , { "linestyle":".-", "linewidth":1 }  
  ]





########################################
# Plot the data
#=======================================
for vi in range( len(vQdata) ):
# xMp.plot( vQdata[vi][1], vQdata[vi][2] )  # Basic Plot Style
# xMp.plot( vQdata[vi][1], vQdata[vi][2], label = vQdata[vi][0] )  # Add legend Labels
  xMp.plot( vQdata[vi][1], vQdata[vi][2], label = vQdata[vi][0], **vLineStyles[vi] )  # Use Own Styles

### Define where the Legend is located or let PyPlot position it
# xMp.legend ( loc = "center left", bbox_to_anchor = ( 1, 0.5 ) )
xMp.legend()

### Label the Chart:
xMp.xlabel( "ETL-Run-Day" )
xMp.ylabel( "ETL-Minutes" )
xMp.title( "Selected ETL Daily Run-Times" )

### Only needed if using x-axis date values.
# xMp.gca().xaxis.set_major_formatter( xMd.DateFormatter( '%b-%d' ) )   
xMp.gca().xaxis.set_major_formatter( xMd.DateFormatter( '%Y-%b-%d' ) )

### Needed to display the created chart:
xMp.show()





#-------------------------------------------------------------------------------
