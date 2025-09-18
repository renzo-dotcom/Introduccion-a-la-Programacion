import random
suma=0
for c in range(5):
    ale=random.randint(0,20)
    print(ale,end=" ")
    suma=suma+ale
prom=suma/5
print("\nLa suma es: ",suma)
print("El promedio es: ",prom)
