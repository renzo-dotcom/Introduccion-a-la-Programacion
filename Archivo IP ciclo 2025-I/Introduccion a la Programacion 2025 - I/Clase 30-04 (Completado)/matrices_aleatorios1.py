"""Calcular una matriz del orden 5x3 con numeros aleatorios"""

import random

for x in range(5): 
    for y in range(3):  
        ale=random.randint(0,9)
        print(ale,end=" ")
    print()  #Esto es para finalizar para cuando acabe esa vuelta de la fila

#La matriz se define por filas con el "x", luego, para determinar la cantidad de numeros que tendrá la fila (columnas), se usará el "y"