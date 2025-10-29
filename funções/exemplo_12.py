import os
os.system("cls")
import math

def conta_vogais(palavras):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in palavras:
        if(letra in vogais):
            contador  +=1
    return contador

texto = input("digite uma palavra:")
print(conta_vogais(texto))
