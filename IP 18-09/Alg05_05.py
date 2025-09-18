q=int(input("Ingrese la cantidad deseada: "))
tipo=float(input("Ingrese el tipo de repuesto: "))
marca=input("Ingrese la marca: ")

match (tipo):
    case 1010 :
        p1=50
        p2=65
        p3=90
    case 1050 :
        p1=60.5
        p2=75.5
        p3=95.5
    case _:
        p1=0
        p2=0
        p3=0

match (marca):
    case "A"|"a":
        precio=p1
    case "B"|"b":
        precio=p2
    case "C"|"c":
        precio=p3