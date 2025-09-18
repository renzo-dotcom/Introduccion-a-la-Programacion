"""Desarrolle la solucion que permita hallar el sueldo a cobrar por un trabajador
semanalmente, sabiendo que este se obtiene con base a su tarifa horaria y a
la cantidad de horas trabajadas. Considere: 
La cantidad de horas trabajadas no puede ser mayor a 40
- Menos de 1000 10% de incremento
- Entre 1000 y 5000 8% de incremento
- Mas de 5000 6% de incremento
"""

qhoras=int(input("Ingrese la cantidad de horas: "))

#Aqui cambia de la primera solucion
while qhoras>40 :
    qhoras=int(input("Ingrese la cantidad de horas: "))
#Hasta aca
th=int(input("Ingrese la tarifa horaria: "))
sueldo=qhoras*th

if sueldo<1000 :
    inc=sueldo*0.10
elif 1000<sueldo<5000 :
    inc=sueldo*0.08
elif sueldo>5000 :
    inc=sueldo*0.06
    
sueldo=sueldo+inc

print("La cantidad de sueldo con incremento es: ",sueldo)