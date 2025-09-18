import random

nombre=input("Ingrese un nombre: ")
apellido=input("Ingrese el apellido paterno: ")
ale=random.randint(1000,10000)

c1=ale//1000
c2=ale//100%10
c3=ale//10%10
c4=ale%10

suma=c1+c2+c3+c4

primnom=nombre[0:2]
ulape=apellido[-3:]
codigo=primnom+ulape+str(suma)

print("\nSu nuevo código será: ",codigo)
