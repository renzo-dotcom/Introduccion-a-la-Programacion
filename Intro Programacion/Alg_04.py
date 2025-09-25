copias=int(input("Ingrese la cantidad de copias: "))

if copias<20 :
    uni=0.10
elif 20<=copias<=50 :
    uni=0.80
elif 50<=copias<=100 :
    uni=0.75
elif copias>100:
    uni=0.65

total=copias*uni
print("El monto a pagar será de: ",total)