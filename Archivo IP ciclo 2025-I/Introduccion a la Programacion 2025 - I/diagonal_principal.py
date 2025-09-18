"""
Mostrar la diagonal principal
"""

for x in range (4):
    for y in range (4):
        if x==y :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()