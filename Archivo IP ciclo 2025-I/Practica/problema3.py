"""Generar aleatorios de 3 cifras hasta que uno empiece en numero par"""

import random
flag=True

while flag :
    ale=random.randint(100,999)
    print(ale)
    if ale//100 %2 ==0 :
        flag=False