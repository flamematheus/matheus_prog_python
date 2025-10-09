import os
os.system("cls")

# Entrada do número como string para facilitar manipulação dos dígitos
numero = input("Digite um número de 3 dígitos (CDU): ")

# Verifica se o número tem exatamente 3 dígitos
if len(numero) == 3 and numero.isdigit():
    # Inverte o número
    invertido = numero[::-1]
    
    # Imprime o número invertido
    print(f"Número invertido: {invertido}")
else:
    print("Erro: Digite um número válido com exatamente 3 dígitos.")
