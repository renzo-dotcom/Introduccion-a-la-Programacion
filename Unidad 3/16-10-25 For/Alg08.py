import random

q=int(input("Ingrese la cantidad de productos llevados: "))
pre=int(input("Ingrese el precio: "))
for x in range (10):

    ic=q*pre
    pid=random.randint(5,10)/100
    id=pid*ic
    ip=ic-id
    mayID=max(id,mayID)
    print("El importe de compra es: ",ic)
    print("El importe de descuento es: ",id)
    print("El importe a pagar es: ",ip)

print("El importe de descuento final es de :",mayID)