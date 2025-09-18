"""Desarrolle la solucion que permite generar n terminos de la siguiente serie, asi como 
la suma de sus terminos
5 8 11 14 17 20 ...(n terminos)
"""

ter=15  #"ter" es la variable que representará los numeros de la serie, se inicializa en 15 porque es el numero inicial
suma=0  #Se inicializa la variable suma, para que despues vaya incrementando

qter=int(input("Ingrese la cantidad de terminos: "))  #"qter" es la cantidad de terminos que se ingresará

for x in range (qter):
    print(ter,end="")
    suma+=ter  #Codigo para determinar la suma de sus numeros, va dando vuelta por cada repeticion, por cada repeticion se va sumando el nuevo termino generado 
    ter-=5  #Codigo para ir disminuyendo la variable "ter" de 5 en 5

    if(x<qter-1):  #Codigo para referirse a alguna de la edicion del ultimo numero de la serie, es qter-1 porque el x empieza en 0
        print(end=", ")  #Codigo para que todos los numero excepto el utimo numero, tengan una coma

print("\nLa suma de los terminos es: ",suma)
