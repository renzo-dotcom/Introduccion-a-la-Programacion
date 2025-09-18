#Desarrolle la solucion que permita ingresar 5 notas y mostrar el promedio de las mismas

suma=0
for x in range (5):
    num=(float(input("Ingrese un numero: ")))
    suma+=num
    prom=suma/5
print("El promedio de las notas es: ",prom)
print()