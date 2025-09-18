# 2: Mostrar la siguiente serie 3   6   9   #12   15   18   #21   24   27

for x in range (3,28,3) :
    if x==12 or x==21 :
        print("#"+str(x),end=" ")
    else:
        print(x,end=" ")