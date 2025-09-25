flag=True

while flag :
    q=int(input("Ingrese la cantidad deseada: "))

    if 1<=q<=50:
        flag=False
    else:
        print("Error, ingrese una cantidad menor a 50")
pre=int(input("Ingrese el precio unitario del producto: "))

ic=q*pre

if ic<50 :
    desc=ic*0.05
elif 50<=ic<=100:
    desc=ic*0.15
elif 100<=ic<=200:
    desc=ic*0.20
elif ic>200:
    desc=ic*0.25

ip=ic-desc
print("El importe será de: ",ic)
print("El descuento será de: ",desc)
print(ip)