"""Generar aleatorios de dos cifrras hasta encontrar uno en el rango de 40-80"""

import random
flag=True

while flag : 
    ale=random.randint(10,99)
    print(ale,end=" ")
    if 40<ale<80 :
        flag=False