q=int(input("Ingrese la cantidad de numeros que desea ingresar: "))

for x in range (q):
    num=int(input("\nIngrese un numero: "))
    u=num%10
    print("La unidad es: ",u) 
    menor=min(menor,num)

print("\nEl menor numero fue: ",menor)
