"""
Desarrolle la solucion que permita ingresar 3 ventas de una tienda y mostrar el importe de compra, el importe de descuento (10% del importe de compra)
y el importe a pagar de cada una de ellas, asi como, el mayor importe a pagar registrado
"""
mayor=0
for x in range (3):
    print("Venta",x+1)
    pre=int(input("Ingrese el precio: "))
    q=int(input("Ingrese una cantidad: "))
    ic=pre*q
    id=ic*0.10
    ip=ic-id
    print("El importe de compra es: ",ic)
    print("El importe de descuento es: ",id)
    print("El importe a pagar es: ",ip)
    print()

    mayor=max(mayor,ip)
    #FINPARA, AQUI ACABA LA REPETICION Y SE VUELVE A REPETIR EN OTRA VUELTA
print("El mayor importe a pagar es: ",mayor)
