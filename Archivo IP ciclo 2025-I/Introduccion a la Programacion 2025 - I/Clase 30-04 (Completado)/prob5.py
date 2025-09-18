"""Desarrolle la solucion que permite generar n terminos de la siguiente serie, asi como 
la suma de sus terminos
5 8 11 14 17 20 ...(n terminos)
"""

ter=15
suma=0
#Ya que es n, se ingresa el numero
qter=int(input("Ingrese la cantidad de terminos: "))

for x in range (qter):
    print(ter,end=" ")
    ter-=5
    suma+=ter

print("\nLa suma de los terminos fue: ",suma)
