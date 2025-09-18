"""
Construir la siguiente matriz
0 1 2
1 2 3
2 3 4
3 4 5
4 5 6
"""
#Recordar que para lograr eso, cada numero de la matriz es igual a la suma de su numero de fila y columna

for x in range (5):
    for y in range (3):
        print(x+y,end=" ")  #Se imprime "x+y" para mostrar la suma del numero de su fila y su columna segun su posicion 
    print()