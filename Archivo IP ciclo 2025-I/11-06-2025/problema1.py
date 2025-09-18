"""Desarrolle la solucion que con base a una frase ingresada, permita hallar y mostrar la cantidad de palabras que tiene"""

frase=input("Ingrese una frase que desee: ")

tamaño=len(frase)
if tamaño>0 :
    palabras=1
    
    for i in range(tamaño):
        caract=frase[i]
        if caract==" " :
            palabras=palabras+1
    print(palabras,"palabras")
    
else:
    palabras=0
    print("Usted no ingresó ninguna palabra")