frasep=input("Ingrese una frase: ")
frase=frasep.strip()
long=len(frase)


palabras=0

for x in range (long) :     #x es un numero del total del range
    carac=frase[x]
    if carac==" " :
        palabras=palabras+1
print("El numero de palabras es: ",palabras)
if palabras==0 :
    print("Usted no ingresó ninguna palabra")


