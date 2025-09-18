import random
me=999
suma=0
ccap=0

n=int(input("Ingrese la cantidad de numeros deseados: "))
for x in range (n):
    num=random.randint(100,999)
    me=min(me,num)
    if num//100 == num%10 :
        ccap+=1  
    suma=suma+num
    if num==123 :
        msj="Se generó el numero 123"
    else:
        msj="No se generó el number 123, fly robin fly"
porcap=ccap*100/n
prom=suma/n
print()
print("El numero menor es: ",me)
print("El porcentaje de numeros capicuas es: ",porcap)
print("El promedio de los numeros es: ",prom)
print(msj)