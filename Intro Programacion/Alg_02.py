escuela=input("Ingrese la escuela: ")
esp=input("Ingrese la especialidad deseada :")

match (escuela):
    case "EPI":
        match (esp):
            case "sistemas":
                men=500
            case"electronica":
                men=550
            case "civil":
                men=450
            case _ :
                print("Error")
    case "EPS":
        match (esp):
            case "biologia":
                men=400
            case "sociologia":
                men=350
            case "trabajo social":
                men=300
            case _:
                print("Error")
    case "EPA":
        match (esp):
            case "musica ":
                men=300
            case "teatro":
                men=350
            case "danza":
                men=250
            case _:
                print("Error")
print("El precio será de: ",men)