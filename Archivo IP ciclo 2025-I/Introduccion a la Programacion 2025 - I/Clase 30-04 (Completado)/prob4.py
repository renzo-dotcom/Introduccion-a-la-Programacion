"""Desarrolle la solucion que permita generar n terminos de la siguiente serie:
5 8 11 14 17 20
"""

n=int(input("Ingrese el numero de terminos deseados: "))
ter=5
for x in range(n):
    print(ter,end=" ")
    ter+=3