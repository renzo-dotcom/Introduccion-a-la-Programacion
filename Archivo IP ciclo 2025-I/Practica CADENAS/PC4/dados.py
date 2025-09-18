import random

Jtiro2=0
Ctiro2=0

Jtiro1=random.randint(1,6)
Ctiro1=random.randint(1,6)
print("El primer tiro de Juan dió: ",Jtiro1)
print("El primer tiro de Carlos dio: ",Ctiro1)
if Jtiro1==Ctiro1 :
    Jtiro2=random.randint(1,6)
    Ctiro2=random.randint(1,6)
    print("El segunda tiro de Juan dió: ",Jtiro2)
    print("El segundo tiro de Carlos dio: ",Ctiro2)

puntJuan=Jtiro1+Jtiro2
puntCarlos=Ctiro1+Ctiro2
print("El puntaje total de Juan fue: ",puntJuan)
print("El puntaje total de Carlos dió: ",puntCarlos)

if puntJuan==puntCarlos :
    print("Hubo empate")
elif puntJuan>puntCarlos:
    print("El ganador fue Juan")
elif puntJuan<puntCarlos :
    print("El ganador fue Carlos")