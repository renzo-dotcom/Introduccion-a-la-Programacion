"""
Desarrolle  la solucion que permita hallar y mostrar el procentaje de numeros de 3 digitos ingresados por un usuario
Considere que el usuario decide si desea o no seguir ingresando numeros
"""

rpta="si"
cnum3=0
cnum=0

while rpta=="si" :
    num=int(input("Ingrese un numero: "))

    if num>=100 and num<=999:
        cnum=cnum+1
    print("Eligió: ",rpta)

por=cnum3*100/cnum
print("El porcetaje fue: ",por)