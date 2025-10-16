"""Diseñe la solucion que con base a 10 numeros aleatorios de 2 cifras, 
permita hallar y mostrar el porcentaje de los que fueron pares"""

import random
pares=0

for x in range (10):
    num=random.randint(10,99)
    print(num)
    if num%2==0:
        pares+=1
        

porpar=pares/10
print("El numero de numeros pares fue: ",pares)
print("El porcentaje de pares es: ",porpar)