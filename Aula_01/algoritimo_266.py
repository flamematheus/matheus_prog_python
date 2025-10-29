import os
os.system ("cls")

import time

while True:
    nome = input("Digite um nome (ou 'FIM' para encerrar): ")
    if nome.upper() == "FIM":
        break
    if nome:  # Verifica se o nome não está vazio
        print(f"Primeiro caractere: {nome[0]}")
 
 