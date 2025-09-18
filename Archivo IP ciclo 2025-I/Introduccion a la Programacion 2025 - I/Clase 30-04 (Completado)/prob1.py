"""Desarrolle la solucion que permita generar 10 numeros aleatorios de 1 cifra, en base a ellos mostrar
- El mayor aleatorio
- El menor aleatorio
- El porcentaje de aleatorios que fueron pares
"""


ma=0  #Con esto se aplica la comparacion de inicializacion del numero maximo
me=9
cpares=0
import random

for x in range(10):  #Mostrar la repeticion 10 veces
    ale=random.randint(0,9)  #Valor de variable del aleatorio
    print(ale,end=" ")  #Se muestra el aleatorio

    ma=max(ma,ale)  #Calculo del mayor numero aleatorio generado
    me=min(me,ale)  
    if ale%2==0 :  #Calculo de que el aleatorio es par
        cpares=cpares+1 #Incremento de la variable cada vez que se cumple la condicion de que el numero aleatorio es par
    porc_pares=cpares/10*100  #Calculo del porcenatje de la cantidad total incrementada del numero de pares
print()
print("El mayor aleatorio es: ",ma)
print("El menor aleatorio es: ",me)
print("El porcentaje de aleatorios que fueron pares es: ",porc_pares)