flag=True
all= "" #acumulador=texto
mayor=0
mayor100="" #acumulador=texto
entre=""
mayor1000=""
cont=0 #contador=numerico
pares=0 #contador=numerico
impares=0 #contador=numerico

while (flag):
    num=int(input("Ingrese un número: "))

    all+=str(num)+" "
    eleccion=input("Desea ingresar otro numero?: ")
    cont+=1
    mayor=max(mayor,num)
    if num>100:
        mayor100+=str(num)+" "
    if 100<num<1000:
        entre+=str(num)+" "
    if num>1000:
        mayor1000+=str(num)+" "
    if num%2==0:
        pares+=1
    porcentajepar=pares/cont
    if num%2!=0 :
        impares+=1
    porcentajeimp=impares/cont

    if eleccion=="no":
        flag=False


print("Todos los numeros ingresados fueron: ",all)
print("El numero mayor fue: ",mayor)
print("La cantidad de numeros mayores a 100 fueron: ",mayor100)
print("Los numeros entre 100 y 1000 fueron: ",entre)
print("Los numeros mayores a 1000 fueron: ",mayor1000)
print("El total de numeros ingresados fue: ",cont)
print("La cantidad de numeros pares fueron: ",pares)
print(str("El porcentaje de numeros pares fueron: ")+str(porcentajepar)+str("%"))
print("La cantidad de numeros impares fueron: ",impares)
print(str("El porcentaje de numeros impares fueron: ")+str(porcentajeimp)+str("%"))
