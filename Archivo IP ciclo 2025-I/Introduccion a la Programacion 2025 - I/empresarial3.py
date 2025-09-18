"""Problema:
Una empresa recibe reportes del stock de 10 productos distintos. Necesita:
Ver cuántos productos están agotados (stock = 0)
Cuál producto tiene el mayor stock
El promedio general de stock
"""
cont=0
mayor=0
suma=0 

for x in range (10):
    stock=int(input(str("Ingrese el stock del producto N° ")+str(x+1)+str(" : ")))
    if stock==0 :
        cont+=1
    mayor=max(mayor,stock)
    suma+=stock
    #FIN del bucle
print()
prom=suma/10
print("La cantidad de productos agotados es: ",cont)
print("El producto que tiene mayor stock es: ",mayor)
print("El promedio general de stock es: ",prom)