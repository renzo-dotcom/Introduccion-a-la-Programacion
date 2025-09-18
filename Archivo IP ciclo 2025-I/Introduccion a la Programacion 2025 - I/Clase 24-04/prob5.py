"""
Generar 10 aleatorios de 2 cifras cuando:
- Cuantos fueron menores a 30
- Cuantos estan entre 30 y 60
- Cuantos fueron mayores a 60
"""
import random

cpares=0

for x in range(10):
    ale=random.randint(10,99)
    print(ale,end=" ")

    if ale%2==0:
        cpares+=1
   
print("\nLa cantidad de pares fue: ",cpares)
print()