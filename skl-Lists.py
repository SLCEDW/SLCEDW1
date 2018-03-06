# Python Lists

#===================================================================================================
print( "\n"+80*"="+"\n"+6*"="+" Start of Output "+6*"="+"   "+7*"\*/   "+6*"="+"\n"+80*"="+"\n" )
#===================================================================================================

print( "\n" + "====================> List Manipulation, Length:" + "\n" )

vLst1 = [ 123, "sam", 3.14, 0 ]
vLst2 = [ True, False, 999, ' ', 'end' ]
print( vLst1, "List-Length:", len(vLst1) )
print( vLst2, "List-Length:", len(vLst2) )

vLst3 = vLst1 + vLst2
print( "Concatenation:", vLst3 )

print( "ReAssign Values Before:", vLst3 )
vLst3[6] = -91919 
vLst3[1] = "Sam Gamgee"
vLst3[0] = "xyz"
vLst3[4] = 1
vLst3[7] = False
print( "ReAssign Values  After:", vLst3 )

print( "\n" + "====================> List append, insert:" + "\n" )

vLst5 = [ 3, 4, 5 ]
print( "Before Inserts and Appends:", vLst5 )
vLst5.insert(0,2)
vLst5.insert(0,1)
vLst5.append(6)
vLst5.append(999)
print( "After Inserts and Appends:", vLst5 )

print( "\n" + "====================> Slicing Lists:" + "\n" )

vLst4 = [ "a", "b", "c", "d", "e", "f", "g", "h", "i" ]
print( "Starting List:", vLst4 )
print( "Return the      first 6 elements (< #6)-[:6]:", vLst4[:6] )
print( "Return the  elements from #3 on (>= #3)-[3:]:", vLst4[3:] )
print( "Return the     sub-list (>= #3)&(< #6)-[3:6]:", vLst4[3:6] )
	
vLst4[2:7] = [ 'xxx', 'yyy' ]
print( "Replace a sublist with a different length list:", vLst4 )
vLst4[1:5] = vLst5
print( "Replace a sublist with a different list:", vLst4 )

print( "\n" + "====================> Lists of lists:" + "\n" )

vL = [ 111, 222, 333 ]
vL[0] = [ "bug", "new", "run" ]
vL[1] = [ True, False, True ]
vL[2] = [ 987, -3.14, 0 ]

print("List-in-a-List:", vL)

vL[0][1] = True
vL[1][2] = 123.9
vL[2][0] = "something"

print("Altered:", vL)

#===================================================================================================
print( "\n"+80*"="+"\n"+6*"="+" *End* of Output "+6*"="+"   "+7*"/*\   "+6*"="+"\n"+80*"="+"\n" )
#===================================================================================================
