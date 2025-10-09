import os
os.system("cls")

# Entrada do usuário
saldo = float(input("Digite o saldo da aplicação: R$ "))

# Cálculo do reajuste de 1%
novo_saldo = saldo * 1.01  # ou: novo_saldo = saldo + (saldo * 0.01)

# Impressão do novo saldo
print(f"Novo saldo com reajuste de 1%: R$ {novo_saldo:.2f}")



"""
saldo = float(input("Digite o saldo da aplicação: R$ "))
novo_saldo = saldo + (saldo * 0.01)
print(novo_saldo)

"""