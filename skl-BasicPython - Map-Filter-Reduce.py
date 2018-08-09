import msvcrt 
#===========================================================
# Website: https://www.python-course.eu/python3_lambda.php
#===================================================================================================
print( "\n"+80*"="+"\n"+6*"="+" Start of Output "+"\n"+80*"="+"\n" )
#===================================================================================================




#-------------------------------------------------------------------------------
print("\n"+"="*40+">>> ((( lambda functions )))"+"\n")
#-------------------------------------------------------------------------------

v_fnctn1 = lambda x, y, z : (x + y) * z
print( "Example-1: " + str( v_fnctn1(2,5,3) ) )

v_fnctn2 = lambda a,b : a+b
print( "Example-2: " + str( v_fnctn2(4,7) ) )
  
v_rslt3 = map( lambda x:x*x, (2,3,4,5,6,7,8) ) 
print( list( v_rslt3 ) )



#-------------------------------------------------------------------------------
print("\n"+"="*40+">>> ((( user functions )))"+"\n")
#-------------------------------------------------------------------------------

def deg_c_to_f(t):
  return ((float(9)/5)*t+32)
  
def deg_f_to_c(t):
  return (float(5)/9)*(t-32)

print( deg_c_to_f(0) )
print( deg_f_to_c(212) )



#-------------------------------------------------------------------------------
print("\n"+"="*40+">>> ((( map )))"+"\n")
#-------------------------------------------------------------------------------

print(list(   map(deg_c_to_f, {-40, 0, 32, 100})   ))
print(list(   map(deg_f_to_c, [-40, 0, 32, 100])   ))

a = [ 2, 3, 4, 5 ]
b = [ 34, 52, 39, 27 ]
c = [ 7, 9, 0, 8 ]
d = list(map( lambda x,y,z : y-(x*z)   ,   a,b,c ))
print(d)



#-------------------------------------------------------------------------------
print("\n"+"="*40+">>> ((( filter )))"+"\n")
#-------------------------------------------------------------------------------

v_list = [ 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 ]
v_odds = list(filter( lambda x: (x%2)!=0 , v_list ))
print( "Odd Numbers: ", v_odds)  

v_fives = list(filter( lambda x: (x%5)==0 , v_list ))
print( "Multiples of Five: ", v_fives)  
  


#-------------------------------------------------------------------------------
print("\n"+"="*40+">>> ((( reduce )))"+"\n")
#-------------------------------------------------------------------------------

from functools import reduce
v_list = [ 4, 6, 5, 3, 7 ]
v_sum = reduce( lambda x,y: x+y, v_list )
print( "Add the elements up:", v_sum )

v_rslt = reduce( lambda x,y: x if (x>y) else y, v_list )
print( "Largest element:", v_rslt )

v_rslt = reduce( lambda x,y: x if (x<y) else y, v_list )
print( "Smallest element:", v_rslt )

v_lo = 1342
v_hi = 275481
v_sum_all = reduce( lambda x,y : x+y,  range( v_lo, v_hi + 1 ) )
v_calc = (v_hi-v_lo+1)*(v_lo+v_hi)/2
print( "Sum Range by REDUCE:", v_sum_all, "     Calculation:", v_calc )



#===================================================================================================
print( "\n"+80*"="+"\n"+6*"="+" End of Output "+"\n"+80*"="+"\n" )
#===================================================================================================
print( "Any Key to Exit: " )
v_null = msvcrt.getch()
