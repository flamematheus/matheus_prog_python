import math
import os
os.system("cls")

def somar(a,b):
    total = a+b
    print(total)

def subtrair(a,b):
    total = a-b
    print(total)

def multiplicar(a,b):
    total = a*b
    print(total)

def dividir(a,b):
    total = a/b
    print(total)


numero_01 = int(input("digite um numero :"))
numero_02 = int(input("digite um numero :"))

op = input("digite a operação")

if (op =="+"):
        somar(numero_01,numero_02)
elif(op =="-"):
     subtrair(numero_01,numero_02)
elif(op =="*"):
     multiplicar(numero_01,numero_02)
elif(op =="/"):
     dividir(numero_01,numero_02)
else:
     print("operação invalida !!")


#somar(numero_01,numero_02)