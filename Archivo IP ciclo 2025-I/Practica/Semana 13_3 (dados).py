"""Dos jugadores cada uno lanza un dado, si hay empate lanzan otro dado cada uno de ellos.
Mostrar puntaje de cada uno, y quien ganó o si hubo empate"""

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