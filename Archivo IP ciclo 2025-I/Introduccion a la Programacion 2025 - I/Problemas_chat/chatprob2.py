#Problema 6: Números capicúas de 100 a 999 con coma cada numero, excepto el ultimo numero

for x in range (100,1000):
    if x//100 == x%10 :
        if x<999 :
            print(x,end=", ")
        else :
            print(x,end=" ")
