"""Desarrolle la solucion que permita hallar y mostrar la cantidad de vocales que tiene un frase"""

frase=input("Ingrese una frase que desee: ")

long=len(frase)

letra=1

for x in range (long):
    caract=frase[x]
    if caract=='a' or caract=='A' :
        letra=letra+1
print(letra,"letras")


        