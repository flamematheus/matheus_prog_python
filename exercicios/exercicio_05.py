import os
os.system("cls")

a = int(input("digite um numero :"))
b= int(input("digite um numero :"))
c = int(input("digite um numero :"))

def calcular_valores(a,b,c):
    dobro= a*2
    dobrob= b*2
    dobroc= c*2
    return dobro,dobrob,dobroc 

print(calcular_valores(a,b,c))
