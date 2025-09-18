"""Mostrar numero aleatorios de 3 cifras hasta encontrar uno cuya primera cifra sea par"""

import random 
flag=True

while flag :
    ale=random.randint(100,999)
    print(ale,end=" ")
    if ale//100 %2 ==0 :
        flag=False