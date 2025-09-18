"""
Desarrolle la solucion que permita ingresar 3 ventas de una tienda y mostrar el importe de compra, el importe de descuento (10% del importe de compra)
y el importe a pagar de cada una de ellas, asi como, el mayor importe a pagar registrado
"""
mayor=0
for x in range(3):
    #Se ingresan las variables complementarias
    precio=int(input(str("Ingrese el precio de la venta ")+str(x+1)+str(" : ")))
    q=int(input("Ingrese la cantidad: "))
    #Operaciones
    ic=precio*q
    id=ic*0.10
    ip=ic-id
    #Se imprimen las variables
    print("El importe de compra es: ",ic)
    print("El importe de descuento es: ",id)
    print("El importe a pagar es: ",ip)

    mayor=max(mayor,ip)
    print()
print("El mayor importe es: ",mayor)