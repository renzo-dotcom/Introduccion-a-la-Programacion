"""Ingrese numero mientras el usuario lo desee"""
#El while funciona mientras la condicion sea verdadera

flag=True
while(flag):
    num=int(input("Ingrese un numero: ")) 
    rpta=int(input("Desea ingresar otro numero? 1=SI 0=NO: "))
    
    if rpta==0:
        flag=False 