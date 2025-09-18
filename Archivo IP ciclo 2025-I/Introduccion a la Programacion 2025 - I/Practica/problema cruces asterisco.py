for x in range (5):
    for y in range (5):
        if x==y or x+y==4 :
            print("*",end=" ")
        else: 
            print(" ",end=" ")
    print()
       

"""
00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
30 31 32 33 34
40 41 42 43 44
"""