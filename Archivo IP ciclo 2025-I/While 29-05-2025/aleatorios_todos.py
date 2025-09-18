"""Desarrolle la solucion que permite generar 10 aleatorios pares de 2 cifras"""

import random
allnum=""
cont=0


while (cont<10) :
    ale=random.randint(10,99)
    if ale%2==0 :
        cont+=1
        print(ale, end=" ")
        
    allnum=allnum+str(ale)+" "
    
print()
print("Todos los numeros que se generaron hasta llegar a 10 pares y parar fueron: ",allnum)
    