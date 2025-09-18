flag = True
numeros=" " 

while flag:
    num = int(input("Ingrese un número: "))
    numeros+= str(num)+" " 
    eleccion = input("Desea ingresar otro número?: ")
    if eleccion== "no":
        flag = False

print("Los números ingresados son:", numeros)
