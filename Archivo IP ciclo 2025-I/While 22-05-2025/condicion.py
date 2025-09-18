"""Hallar el importe de compra, el importe de descuento y el importe a pagar, si el importe de descuento es del 10%,
y como maximo se pueden comprar 10 productos"""

qpro=int(input("Ingrese la cantidad de productos: "))

if (qpro>10):
    print("Error")
else: 
    pre=int(input("ingrese el precio: "))
    ic=pre*qpro
    id=ic*0.10
    ip=ic-id
    print("El importe de compra es: ",ic)
    print("El importe de descuento es: ",id)
    print("El importe a pagar es: "),ip
    
    