num1=int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
oper=input("Ingrese el operador: ")

match (oper):
    case "+": res=num1+num2
    case "-": res=num1-num2
    case "*": res=num1*num2
    case _: res=0
print ("El resultado es: ",res)