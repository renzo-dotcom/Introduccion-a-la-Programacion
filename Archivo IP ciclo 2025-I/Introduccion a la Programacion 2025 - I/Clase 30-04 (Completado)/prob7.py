"""Desarrolle lla solucion que permite generar 13 terminos de la siguiente serie
5/2 8/4 11/6 14/8 17/10 20/12
"""

#Primero que todo, calcular cual es la constante de la serie
#La constante es que el numerador se incrementa de 3 en 3, y el denominador de 2 en 2


nu=3
de=2
suma=0

for x in range (13):
    print(str(nu)+"/"+str(de),end=" ")    #str se concatena con +

    suma+=nu/de

    nu+=3
    de+=2
print("\nLa suma es: ",suma)