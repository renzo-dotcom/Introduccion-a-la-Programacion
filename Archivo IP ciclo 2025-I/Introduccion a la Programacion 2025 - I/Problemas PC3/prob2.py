#Desarrolle la solucion que permita generar y mostrar la siguiente serie: 4 #8 12 #16 20 #24 28 nTerminos
num=0
n=int(input("Ingrese el numero de terminos deseado: "))
for x in range (n):
    num+=4
   
    if num%8==0 :
        print(str("#")+str(num),end=" ")
    else:
        print(num, end=" ")