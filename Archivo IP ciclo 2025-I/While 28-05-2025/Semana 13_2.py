"""Desarrolle la solucion que permita generar la siguiente serie y
la suma de sus terminos. Considere que la cantidad de terminos
no puede ser menor a 3 ni mayor a 15 

2/2, 4/3, 8/4, 16/5, 32/6, ...
"""

flag=True
suma=0

while (flag):
    qter=int(input("Ingrese la cantidad de terminos deseada : "))
    if qter>=3 and qter<=15 :
        flag=False
        
nu=2
de=2
for x in range (qter):
    print(str(nu)+"/"+str(de),end="")

    if x<qter-1 : #Condicion para ponerle coma a todos los numeros excepto al ultimo
        print(", ",end="")
        
    suma+=nu/de 
    suma=round(suma,2)
    nu*=2
    de+=1
    
print("\nLa suma es: ",suma)