"""
Una tienda registra sus ventas diarias en una semana (7 días) con numeros aleatorios del 0 al 20. El gerente quiere saber:
El total de ventas de la semana.
El día que tuvo la mayor venta.
El promedio de ventas diarias
"""
suma=0
mayor=0
for x in range (7):
    venta=int(input(str("Ingrese las ventas del día ")+str(x+1)+str(": ")))
    mayor=max(mayor,venta)
    suma+=venta
    #FIN del bucle
prom=suma/7
print("La mayor cantidad de ventas registradas en un día es: ",mayor)
print("El promedio de ventas diarias es: ",prom)