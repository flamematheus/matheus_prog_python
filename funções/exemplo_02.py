import math
import os
os.system("cls")

def somar(a,b ):
    total = a+b
    return total

def raizQuadrada(a):
    raiz = math.sqrt(a)
    print(raiz)

#----------------------------------------------#

print("função informando o valor dos paremetros")

nun_01 = int(input("digite um numero :"))
nun_02 = int(input("digite um numero :"))

print("função somar rebendo os parametros")

raiz2 = somar(nun_01,nun_02)

print("função raiz quradara recebendo o retorno  da função somar")
raizQuadrada(raiz2)