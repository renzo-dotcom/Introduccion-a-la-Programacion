#INGRESO DE NUMEROS

flag=True

pares=0
mayor=0
menores100=0
entre=0
mayor1000=0

while flag :
    num=int(input("Ingrese un numero: "))
    mayor=max(mayor,num)
    if(num>1000):
        mayor1000+=1
    elif(100<=num<=1000):
        entre+=1
    elif num<100 :
        menores100+=1
    elif num%2==0 :
        pares+=1

    eleccion=input("Desea ingresar otro numero? Elija si o no: ")
    if eleccion=="si":
        flag=True
    elif eleccion=="no":
        flag=False
        print("La cantidad de numeros pares que ingresó fue: ",pares)
        print("El mayor numero fue: ",mayor)
        print("Los numeros menores a 100 fueron: ",menores100)
        print("Los numeros entre 100 y 1000 fueron: ",entre)
        print("Los numeros mayores a 1000 fueron: ",mayor1000)

