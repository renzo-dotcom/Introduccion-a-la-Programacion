"""Dos jugadores cada uno lanza un dado, si hay empate lanzan otro dado cada uno de ellos.
Mostrar puntaje de cada uno, y quien ganó o si hubo empate"""

import random
d3=0  #Inicializando 
d4=0

d1=random.randint(1,6)
d2=random.randint(1,6)

if d1==d2 : #Si son iguales significa que hay empate, por lo que cada uno vuelve a lanzar los dados
    d3=random.randint(1,6)
    d4=random.randint(1,6)
    
pf1=d1+d3  #pf=puntaje final
pf2=d2+d4

if pf1>pf2 :
    msj="Ganó el jugador 1"
elif pf1<pf2 :
    msj="Ganó el jugador 2"
else:
    msj="Hubo empate"
    
print("El puntaje final del jugador 1 es: ",pf1)
print("El puntaje final del jugador 2 es: ",pf2)
print(msj)


#MENÚ 

flag=True

while (flag):
    flagOpcion=True
    
    print("[1] Gráfico")
    print("[2] Serie")
    print("[3] Dados")
    print("[4] Salir")
    
    while (flagOpcion):
        opc=int(input("Seleccione la opcion deseada: "))
        if opc>=1 and opc<=4 :
            flagOpcion=False  #Con esto se corta
            
    match (opc):
        case 1:
            print("Se seleccionó la opción 1")
        case 2:
            print("Se seleccionó la opcion 2")
        case 3 :
            print("Se seleccionó la opcion 3")
        case _ :
            flag=False
            print("Gracias por utilizar el menú")