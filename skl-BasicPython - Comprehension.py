import msvcrt 
#===========================================================
# Website: https://www.python-course.eu/python3_list_comprehension.php
#===================================================================================================
print( "\n"+80*"="+"\n"+6*"="+" Start of Output "+"\n"+80*"="+"\n" )
#===================================================================================================
#
# List Comprehensions: made to replace lambda functions, filter(), map(), reduce()
#
#===================================================================================================





#-------------------------------------------------------------------------------
print("\n"+"="*40+">>> ((( List Comprehension Example: Temperature Conversion )))"+"\n")
#-------------------------------------------------------------------------------

v_Temp_C = [ -40, 0, 21.5, 37, 100 ]
v_Temp_F = [ round((float(9)/5)*t+32, 2)   for t in v_Temp_C ]
v_revert = [ round((float(5)/9)*(t-32), 2)   for t in v_Temp_F ]
print( " Start with Celsius Temps:", v_Temp_C )
print( "Convert all to Fahrenheit:", v_Temp_F )
print( "  Revert to initial temps:", v_revert )



#-------------------------------------------------------------------------------
print("\n"+"="*40+">>> ((( List Comprehension Example: Pythagorean Tripples )))"+"\n")
#-------------------------------------------------------------------------------

v_p3 = [ 
  (x, y, z) 
  for x in range(1,20) 
  for y in range(1,20) 
  for z in range(1,20) 
  if x**2 + y**2 == z**2
  and y >= x ]
print( "Pythag-Tripples:", v_p3 )



#-------------------------------------------------------------------------------
print("\n"+"="*40+">>> ((( List Comprehension Example: String Concatenations )))"+"\n")
#-------------------------------------------------------------------------------

v_chr = [ "a", "=", "#" ]
v_num = [ 2, 3, 4 ]
v_combo = [ (i*j)  for i in v_chr  for j in v_num  ]
print( "Character List:", v_chr )
print( "Number of Reps:", v_num )
print( "Other function:", v_combo )



#-------------------------------------------------------------------------------
print("\n"+"="*40+">>> ((( Using Generator () not List [] )))"+"\n")
#-------------------------------------------------------------------------------

v_gen = ( i**3   for i in range(9) )
print( "Generated - Object:",       v_gen   )
print( "Generated Expanded:", list( v_gen ) )



#-------------------------------------------------------------------------------
print("\n"+"="*40+">>> ((( Example: Primes 1 )))"+"\n")
#-------------------------------------------------------------------------------

v_composite = [ j  for i in range(2, 8)  for j in range(i*2, 20, i) ]
print( "Composites:", v_composite )
v_primes = [ x  for x in range(2, 20)  if x not in v_composite ]
print( "Prime List:", v_primes )



#-------------------------------------------------------------------------------
print("\n"+"="*40+">>> ((( SET Comprehension Example: Primes 2 )))"+"\n")
#-------------------------------------------------------------------------------

from math import sqrt
vMax = 50

vComposite = { j
  for i in range(2, int(sqrt(vMax))+1)  
  for j in range(i*2, vMax, i)   }
print( "Composits - No Dups:", vComposite )

vPrime = { i  for i in range(vMax)  if i not in vComposite }
print( "Primes -- in a {Set}:", vPrime ) 

vPrimeSorted = sorted(vPrime)
print( "Primes Sorted [List]:", vPrimeSorted ) 



#-------------------------------------------------------------------------------
print("\n"+"="*40+">>> ((( Using Recursion )))"+"\n")
#-------------------------------------------------------------------------------

from math import sqrt

def f_Primes( n ):
  if ( n == 0  or  n == 1 ):  return []
  else:
    v_pl = f_Primes( int( sqrt(n) ) )
    v_no = { j  for i in v_pl  for j in range( i*2, n+1, i ) }
    v_pl = { x  for x in range(2, n + 1)  if x not in v_no }
  return v_pl

vPrimeSorted = sorted( f_Primes(80) )
print( "Prime-List:", vPrimeSorted )
    


#===================================================================================================
print( "\n"+80*"="+"\n"+6*"="+" End of Output "+"\n"+80*"="+"\n" )
#===================================================================================================
print( "Any Key to Exit: " )
v_null = msvcrt.getch()
