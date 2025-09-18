flag=True

while (flag):
    flagOpcion=True
    print("[1] Juego")
    print("[2] Matriz")
    print("[3] Dados")
    print("[4] Salir")

    while (flagOpcion):
        opc=int(input("Ingrese la opcion deseada: "))
        if opc>1 and opc <4 :
            flagOpcion=False
"""
    match (opc):
        case 1:
            #START
"""