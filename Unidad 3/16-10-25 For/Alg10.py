import random
cap=0
q=int(input("Ingrese la cantidad de cifras que desea ingresar: "))
for x in range (q) :
    ale=random.randint(100,999)
    print(ale)
    u=ale%10
    c=ale//100
    if u==c :
        cap+=1

print("La cantidad de numeros capicuas fueron: ",cap)
tcap=cap
prom=cap/q
print("El promedio de numeros capicuas es: ",prom)


"chrome-extension://aomkpefnllinimbhddlfhelelngakbbn/Game_Source/index.html"