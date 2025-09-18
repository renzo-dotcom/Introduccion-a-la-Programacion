"""Solucion que permita ingresar numeros hasta que el usuario lo desee"""

flag=True

while flag : 
    num=int(input("Ingrese un numero: "))
    eleccion=int(input("Desea ingresar otro numero? Marque 1 para responder SI, marque 0 para elegir NO: "))

    if eleccion==0 :
        flag=False