"""Desarrolle la solucion que permita hallar el sueldo a cobrar por un trabajador
semanalmente, sabiendo que este se obtiene con base a su tarifa horaria y a
la cantidad de horas trabajadas. Considere: 
La cantidad de horas trabajadas no puede ser mayor a 40
- Menos de 1000 10% de incremento
- Entre 1000 y 5000 8% de incremento
- Mas de 5000 6% de incremento
"""
qh=int(input("Ingrese la cantidad de horas trabajadas: "))


while qh>40 :                                                                 
    qh=int(input("Ingrese la cantidad de horas trabajadas: "))

th=int(input("Ingrese la tarifa horaria: "))
sueldo=qh*th
if sueldo < 1000 :
    sinc=sueldo*1.10
elif 1000<sueldo<5000 :
    sinc=sueldo*1.08
elif sueldo>5000 :
    sinc=sueldo*1.06
print("El sueldo a cobrar es: ",sinc)




"""
Opcion de flag en while

while (flag):
    qh=int(input("Ingrese la cantidad de horas trabajadas: "))
    if qh<=40 :  
        flag=False
"""