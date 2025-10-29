import os
os.system("cls")
import math

def media (lista):
    return sum(lista)/len(lista)


notas =[]

for i in range(5):
    nota = int(input("digite um numero "))
    notas.append(nota)



print(media(notas))