"""
1: Diagonal principal y la diagonal secundaria de una matriz de orden n
2: Mostrar la siguiente serie 3   6   9   #12   15   18   #21   24   27
3: juego de dados
4: salir
"""
            

#[1]

for x in range (5):
    for y in range (5):
        if x==y or x+y==4 :
            print("*",end=" ")
        else: 
            print(" ",end=" ")
    print()
       
#[2]

for x in range (3,28,3) :
    if x==12 or x==21 :
        print("#"+str(x),end=" ")
    else:
        print(x,end=" ")

# [3]

import random

st1=0
st2=0
j1=random.randint(1,6)
j2=random.randint(1,6)
print("El primer tiro del primer jugador dio: ",j1)
print("El primer tiro del segundo jugador dio: ",j2)
if j1==j2 :
    st1=random.randint(1,6)
    st2=random.randint(1,6)

pun1=j1+st1
pun2=j2+st2

if pun1>pun2 :
    msj="el primer jugador"
elif pun1<pun2 :
    msj="el segundo jugador"
elif pun1==pun2 :
    msj="ninguno, hubo tablas"

print()
print("El puntaje del primer jugador fue",pun1)
print("El puntaje del segundo jugador fue",pun2)
print("El ganador fue",msj)

#[4]