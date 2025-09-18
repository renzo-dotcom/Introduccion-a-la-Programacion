"""Desarrolle la serie que permita generar la siguiente serie 
5, 8, 11, 14, 17, 20
"""
#Cuantos numero son de la serie? 6 (pero eso no importa si vas a utiliza los 3 indicadores en el rango.
#Por cual empieza? En 5. Cual es el numero final? El 20. Cual es la constante de la serie? 3 en 3
#Primero tienes que identificar cual es la constante, ya está
#Primero, los numeros van de 3 en 3
#Segundo, Castillo xd hijo de la U, En este caso es que todos los numero van acompañados con una coma excepto el ultimo numero, 
#por eso el ultimo numero tendrá una condicion especial 

for x in range (5,21,3):
    print(x,end="")

    if x<20 :
        print(end=", ")