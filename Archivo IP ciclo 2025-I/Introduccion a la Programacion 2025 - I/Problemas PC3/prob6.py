#Desarrolle una solucion que permita generar un grafico de orden n, conformado por aleatorios de una cifra y mostrar la suma de los terminos
#de la diagonal principal

import random
suma=0

n=int(input("Ingrese el orden de la matriz cuadrada: "))
for x in range (n):
    for y in range (n):
        ale=random.randint(0,9)
        print(ale,end=" ")
       
        if(x+y==n-1):
            suma=suma+1
               
    print()
print("La suma de la diagonal secundaria es igual a: ",suma)

