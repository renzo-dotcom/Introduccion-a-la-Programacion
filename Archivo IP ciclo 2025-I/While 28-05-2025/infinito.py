import random
flag=True
num=int(input("Ingrese el tiro mostrado: "))
while flag :
    dado=random.randint(1,10000)
    print(dado)
    if num==dado :
        flag=False  