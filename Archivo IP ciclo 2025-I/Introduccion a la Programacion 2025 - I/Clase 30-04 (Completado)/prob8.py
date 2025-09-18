"""Desarrolle la solucion que permite generar 7 terminos de la siguiente serie, asi como la suma de sus terminos
5/2 8/-4 11/8 14/16 ...
"""

#Primero que todo, calcular cual es la constante de la serie
#La constante es que el numerador se incrementa de 3 en 3, y el denominador se va multiplicando por -2


nu=5  #variable numerador
de=2  #variable denominador 
suma=0

for x in range (7):
    print(str(nu)+"/"+str(de),end=" ")    #str se concatena con +

    suma+=nu/de

    nu+=3
    de*=-2
print("\nLa suma es: ",suma)