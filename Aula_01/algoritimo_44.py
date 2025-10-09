import os
os.system("cls")

import math

# Entrada do usuário
numero = float(input("Digite o número (deve ser > 0): "))
base = float(input("Digite a base do logaritmo (deve ser > 0 e ≠ 1): "))

# Verificação de validade
if numero > 0 and base > 0 and base != 1:
    log_resultado = math.log(numero, base)
    print(f"\nLogaritmo de {numero} na base {base} é: {log_resultado:.6f}")
else:
    print("\nErro: o número deve ser > 0 e a base deve ser > 0 e diferente de 1.")


""""
numero = float(input("Digite o número (deve ser > 0): "))
base = float(input("Digite a base do logaritmo (deve ser > 0 e ≠ 1): "))

logoritmo = math.log(numero,base)
print(logoritmo)


"""