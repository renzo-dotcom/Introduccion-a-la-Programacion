nota=int(input("Ingrese la nota del alumno: "))

if 90<=nota<=100 :
    msj="Sobresaliente"
elif 75<=nota<=89 :
    msj="Aprobado"
elif 60<=nota<=74 :
    msj="Suficiente"
elif 50<=nota<=59 :
    msj="Reprobado"
elif 50>nota :
    msj="Reprobado sin opcion a recuperación"
else :
    msj="Error, ingrese un numero de 0 a 100"

print(msj)