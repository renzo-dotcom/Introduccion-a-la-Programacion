#Problema 5: Contar cuántos múltiplos de 5 hay entre 1 y 1000 que también son múltiplos de 3

cont=0
for x in range (1,1001):
    if x%5==0 and x%3==0 :
        cont+=1
print("La cantidad de numero que son multiplos de 5 y 3 son: ",cont)