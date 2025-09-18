Flag=True

while (flag):
    stock=int(input("Ingrese su monto inicial: "))
    if stock>999999 :
        print("Error, el stock no puede superar 999999")
    else:
        flag=True
flagopc=True
qdeposi=0
qretiros=0
stockdeposi=0
while (flagopc):
    print("Su monto total es de: ",stock)
    print("[1] Retiro")
    print("[2] Depósito")
    print("[3] Saldo")
    print("[4] Historia de depositos")
    print("[5] Historia de retiros")
    print("[6] Promedio")
    opcion=int(input("Ingrese el valor que desea depositar: "))

    match(opcion):
        case 1:
            while (op):
                retiro=int(input("Ingrese el valor que desea retirar: "))
                if (stock-retiro>=0):
                    print("Por favor ingrese un retiro válido")
                else:
                    stock=stock-retiro
                    qretiros+=1
                    op=False
        case 2 :
            op2=True
