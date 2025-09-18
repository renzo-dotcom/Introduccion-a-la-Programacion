#Desarrolle la solucion que permita generar y mostrar la siguiente serie: 4 #8 12 #16 20 #24 28 nTerminos
n=int(input("Ingrese la cantidad de numeros deseada: "))
ter=0 

for x in range (n):
    if (x%2!=0): #Condicion de si es impar, aquí "x" se refiere al valor posicional de "x", al valor del numero de repeticion 
        print("#"+str(ter),end=" ") #Imprime eso si el valor posicional de x es impar
    else:
        print(ter,end=" ")

    ter+=4 #Incrementar la variable "ter" de 4 en 4, dandole un valor inicial de 0 porque sí
print("\n") #Solo para dejar espacio en el terminal

