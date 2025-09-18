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
            flagOpcion=False  #Con esto se corta la repeticion de pedir un numero valido


            
    match (opc):
        case 1:
            print("Se seleccionó la opción 1")
            for x in range (5):
                for y in range (5):
                    if x==y or x+y==4 :
                        print("*",end=" ")
                    else: 
                        print(" ",end=" ")
                print()

        case 2:            
            print("Se seleccionó la opcion 2")
            for x in range (3,28,3) :
                if x==12 or x==21 :
                    print("#"+str(x),end=" ")
                else:
                    print(x,end=" ")

        case 3 :
            print("Se seleccionó la opcion 3")
            import random

            st1=0
            st2=0
            j1=random.randint(1,6)
            j2=random.randint(1,6)
            print("El primer tiro del primer jugador dio: ",j1)
            print("El primer tiro del segundo jugador dio: ",j2)
            if j1==j2 :
                st1=random.randint(1,6)
                st2=random.randint(1,6)

            pun1=j1+st1
            pun2=j2+st2

            if pun1>pun2 :
                msj="el primer jugador"
            elif pun1<pun2 :
                msj="el segundo jugador"
            elif pun1==pun2 :
                msj="ninguno, hubo tablas"

            print()
            print("El puntaje del primer jugador fue",pun1)
            print("El puntaje del segundo jugador fue",pun2)
            print("El ganador fue",msj)

        case 4 :
            flag=False
            print("Gracias por utilizar el menú")
print()
