"""Desarrolle la solucion que permite generar 10 aleatorios pares de 2 cifras"""

import random
cont=0
flag=True

while (flag) :
    ale=random.randint(10,99)
    if ale%2==0 :
        cont+=1
        print(ale, end=" ")
    elif cont==10 :
        flag=False
    