# Comments

print("\n"+"=======================================================================")
print(     "===== Start of Output =====   \*/  \*/  \*/  \*/  \*/  \*/  \*/   =====")
print(     "======================================================================="+"\n")

print('Hello World !')
print("From Python.")

print( "\n" + "====================> Arithmetic Calculations:" + "\n" )

v_var1 = 83
v_var2 = 5
v_var3 = ( 10 + (v_var1 - 80) * 4 - 2 ) 

print( "               Print Var: " , v_var3
   , "\n  Divide Creates a Float: " , v_var3/6
   , "\n         Int-Part divide: " , v_var3//6 
   , "\n      Mod-Remainder Only: " , 23 % 5
   , "\n        Raise to a Power: " , v_var2 ** 3
   , "\n         Float-Int mixed: " ,        v_var1 * 3.141592 
   , "\n                Rounding: " , round( v_var1 * 3.141592 , 2 )
   )

print( "\n" + "====================> Strings:" + "\n" )

print( "doesn't", 'ESCAPE: doesn\'t', "'", "''", "'''", '"', '""', '"""' )

print("-----")

print( "line feeds look like this: '\n' some\new\nice\nickles" )
print( r'Use "r" to ignore the escape: some\new\nice\nickles' )

print("-----")

print( """   Make multi-line output or strings
   by using tripple quotes.
   Escape to skip the line-feeds. """ )
   
print("-----")

print( """\
   Make multi-line output or strings
   by using tripple quotes.
   Escape to skip the line-feeds. \
""" )

print("-----")

# Below string has an initial line feed (has no "\")
v_str = '''
This is the first line. The slash \
eliminates the hardcoded line-feed.
This is the second line. \
The slash makes these 2 lines into one.
''' # Ends with 2 line-feeds.
print( v_str )

print( 10 * "-=* " + " Repeat a string " * 2 )

print( "" )
v =             "-abcdefghijklmnopqrstuvwxyz"
print( "Index:   012345678901234567890123456  -- Zero is 1st Char.")
print( 'String: "'+v+'"', v[8]+v[5]+v[12]+v[12]+v[15]+v[0]+v[20]+v[8]+v[5]+v[18]+v[5])
print( "" )
print( "Back from the End: ", v[-1], v[-2], v[-3] )
print( "Grab a substring: " + v[22:27], "Start at 22, less than 27." )
print( "Grab a substring: " + v[0:4], "Start at 0, less than 4." )
print( "From 20 on: " + v[20:99999] )
print( "Slice at 5: "+v[:5]+" / "+v[5:], "-- Combined:"+v[:5]+v[5:] )

print( "Length: " + str(len(v)), len(v) )

v_str1 = "This is a TEST."
print( "UpperCase: ", v_str1, v_str1.upper() )
print( "LowerCase: ", v_str1, v_str1.lower() )

v_str2 = "The quick brown dog jumps over the lazy fox."
print( "Count the occurences of a string:", v_str2.count("o") )
print( "Find the occurences of a string:", v_str2.upper().find("BROWN") )
print( "Replace the occurences of a string:", v_str2.replace("quick","dead").replace("dog","moose") )

print( "\n" + "Formatting values into a string: {} float:{} ({}) ... that's it!".format( 999, 4.567, 'string-val' ) )
print( "\n" + "Splitting a string into a list:", "one~two~three~four".split("~" ) )





print('\n'+"=======================================================================")
print(     "===== *End* of Output =====   /*\  /*\  /*\  /*\  /*\  /*\  /*\   =====")
print(     "======================================================================="+'\n')
