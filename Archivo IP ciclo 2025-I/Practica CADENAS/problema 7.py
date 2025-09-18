#Problema 7

nom1=input("Ingrese el primer nombre: ")
nom2=input("Ingrese el segundo nombre: ")

if nom1>nom2 :
    print(str("El orden alfabetico es: ")+str(nom2)+str(", ")+str(nom1))
elif nom1<nom2 :
    print(str("El orden alfabetico es: ")+str(nom1)+str(", ")+str(nom2))