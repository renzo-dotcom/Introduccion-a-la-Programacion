"""Halla numeros aleatorios de dos cifras hasta que salga uno impar"""
#Para cortar con el flag se usa un if

import random
flag=True

while flag :
    ale=random.randint(10,99)
    if ale%2!=0 :
        flag=False
    print(ale,end=" ")