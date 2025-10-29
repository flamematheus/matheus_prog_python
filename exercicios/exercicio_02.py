import os
os.system("cls")



def calcular_valores(a):
    dobro= a*2
    triplo =a*3
    return dobro , triplo

numero = int(input("digite um numero :"))
print(calcular_valores(numero))

