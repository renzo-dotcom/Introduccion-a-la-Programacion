"""
Desarrolle la solucion que permita calcular el porcentaje de numeros que fueron pares sacados de 10 numeros aleatorios de 2 cifras
"""

import random

for x in range (9):
    ale=random.randint(10,99)
    if ale%2==0 :
        cpar=cpar+1
porcp=cpar/10 
print(porcp)