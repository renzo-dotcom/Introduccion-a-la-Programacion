import random

ale=random.randint(1,3)
if ale==1 :
    correo="@gmail.com"
elif ale==2 :
    correo="@hotmail.com"
elif ale==3 :
    correo="@yahoo.com"

for x in range (3):
    nom1=input("Ingrese el primer nombre: ").lower()
    priap1=input("Ingrese el apellido paterno: ")
    segap1=input("Ingrese el apellido materno: ")

    numale=random.randint(0,100)
    corr=str("26")+str(numale)

    priletra=nom1[0]
    segletra=priap1.lower()
    terletra=nom1[-1]
    print(str("El correo es: ")+str(priletra)+str(segletra)+str(terletra)+str(corr)+str(correo))