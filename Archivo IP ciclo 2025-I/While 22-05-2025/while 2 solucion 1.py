qpro=int(input("Ingrese la cantidad de productos: "))

while qpro>10 :
    print("La maxima cantidad de productos es 10 xd")
    qpro=int(input("Ingrese la cantidad de productos: "))
    
pre=int(input("ingrese el precio: "))
ic=pre*qpro
id=ic*0.10
ip=ic-id

print("El importe de compra es: ",ic)
print("El importe de descuento es: ",id)
print("El importe a pagar es: ",ip)