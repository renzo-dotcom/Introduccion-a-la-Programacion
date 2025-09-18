"""
Una tienda registra sus ventas diarias en una semana (7 días) con numeros aleatorios del 0 al 20. El gerente quiere saber:
Mostrar las ventas de cada día
El total de ventas de la semana.
El día que tuvo la mayor venta.
El promedio de ventas diarias
"""
import random
suma=0
mayor=0
for x in range (7):
    venta=random.randint(0,20)
    print(str("La venta del dia ")+str(x+1)+str(" es: ")+str(venta))
    mayor=max(mayor,venta)
    suma+=venta
    #FIN del bucle
prom=suma/7
print("La mayor cantidad de ventas registradas en un día es: ",mayor)
print("El promedio de ventas diarias es: ",prom)