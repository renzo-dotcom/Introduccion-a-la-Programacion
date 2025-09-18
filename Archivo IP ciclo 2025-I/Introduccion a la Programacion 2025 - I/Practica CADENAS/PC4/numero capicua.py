import random

flag=True
while flag :
    ale=random.randint(100,999)
    print(ale,end=" ")
    if ale//100==ale%10 :
        flag=False