"""
1: Diagonal principal y la diagonal secundaria de una matriz de orden n
2: Mostrar la siguiente serie 3   6   9   #12   15   18   #21   24   27
3: juego de dados
4: salir
"""

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