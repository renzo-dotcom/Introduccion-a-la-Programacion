"""Halla numeros de dos cifras hasta que salga uno impar"""

import random
xd=0
ale=random.randint(10,99)
while ale%2==0 :
    ale=random.randint(10,99)
    if xd :
        flag=False