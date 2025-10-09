import os
os.system("cls")

import math

# Entrada do usuário
numero = float(input("Digite um número positivo: "))

# Verifica se o número é válido
if numero > 0:
    log_base10 = math.log10(numero)
    print(f"O logaritmo de {numero} na base 10 é: {log_base10:.6f}")
else:
    print("Erro: o logaritmo só é definido para números maiores que zero.")



"""
numero = float(input("Digite um número positivo: "))
logaritimo = math. log10(numero)
print(logoritimo)

"""