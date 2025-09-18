#Problema 5
import random

frasepri=input("Ingrese una frase: ")
frase=frasepri.strip()
long=len(frase)

ale=random.randint(0,long)

for x in range (ale):
    carac=frase[x]

print("La posicion aleatoria elegida es: ",x)
print("La letra obtenida aleatoriamente es: ",carac)