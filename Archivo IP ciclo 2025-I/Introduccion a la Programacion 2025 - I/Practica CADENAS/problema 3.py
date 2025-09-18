frasepri=input("Ingrese una frase: ")   #Para extraer una letra de la frase, se usa frase[num de orden de la letra], ejemplo frase[3]
frase=frasepri.strip()
long=len(frase) 

letras=0
for x in range (long):
    carac=frase[x]
    if carac=="a" or carac=="A":
        letras=letras+1
print("El numero de letras a es: ",letras)