"""
Desarrolle la solucion que permita hallar y mostrar el puntaje de calificacion mensual de los 3 miembros de una asociacion sabiendo que:

Puntaje 1 está en base al porcentaje de asistencias (30 dias mensuales)
<30% de inasistencias 2 puntos
Entre 30% y 60% de asistencias 3 puntos
Mas del 60% de asistencias 5 puntos

Puntaje 2 en base a los años de asociado que es un aleatorio de 1 a 5

Puntaje 3 en base a la sede
Sede1 = 2 puntos
Sede2 = 3 puntos
Sede3 = 5 puntos

Puntaje total es igual a la suma de los tres puntajes

Mostrar el puntaje total de cada miembro, asi como el menor y el mayor puntaje total obtenidos
"""

# Okay, a cada miembro tengo que sacarle los 3 puntajes, por lo que se va a repetir 3 veces

import random
punt1=0
punt2=0
punt3=0
for x in range (3):
    print("MIEMBRO",x+1)
    asist=int(input("Ingrese el numero de asistencias: "))
    porAs=(asist/30)*100
    if (porAs<30):
        punt1+=2
    elif (30<porAs<60):
        punt1+=3
    elif (porAs>60):
        punt1+=5
    print("El puntaje 1 es: ",punt1)
    print()
    
    punt2=random.randint(1,5)
    print("El puntaje 2 es: ",punt2)
    print()
    
    sede=int(input("Ingrese la sede: "))
    if sede==1:
        punt3=2
    elif sede==2:
        punt3=3
    elif sede==3:
        punt3=5
    print("El puntaje 3 es: ",punt3)
    print()
    total=punt1+punt2+punt3
    print("El puntaje total es",total)
    menor=min(punt1,punt2,punt3)
    mayor=max(punt2,punt2,punt3)
    print("El puntaje mayor es: ",mayor)
    print("El puntaje menor es: ",menor)
    print()


    