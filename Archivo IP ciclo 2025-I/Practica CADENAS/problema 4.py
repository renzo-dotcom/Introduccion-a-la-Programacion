#Problema 4

frasepri=input("Ingrese una frase: ")
frase=frasepri.strip()
long=len(frase)

vocal=0
for x in range (long):
    carac=frase[x]
    if carac=="a" or carac=="e" or carac=="i" or carac=="o" or carac=="u" :
        vocal=vocal+1
print("La cantidad de vocales es: ",vocal)