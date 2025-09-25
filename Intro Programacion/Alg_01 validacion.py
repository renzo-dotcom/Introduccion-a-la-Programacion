flag = True

while flag:
    nota= int(input("Ingrese la calificación: "))
    
    if nota>=0 and nota<=100:
        flag = False   # valor válido, apagamos la bandera
    else:
        print("Calificación no válida. Debe estar entre 0 y 100")


if nota>= 90:
    print("Clasificación: Sobresaliente")
elif nota>= 75:
    print("Clasificación: Aprobado")
elif nota>= 60:
    print("Clasificación: Suficiente")
elif nota>= 50:
    print("Clasificación: Reprobado, pero puede optar a recuperación")
else:
    print("Clasificación: Reprobado sin opción a recuperación")
