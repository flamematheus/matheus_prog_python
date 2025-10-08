import os 
os.system("cls")

# Função len() = conta o tamanho da string

texto = "olá mundo !"
tamanho =  len(texto)

print(f" o tamanho da string :{tamanho}")

#texto todo em letra maiuscula

texto_maiusculo = texto.upper()


print(f" o texto em letra  maiusculo :{texto_maiusculo}")

#texto todo em letra minusculo

texto_minusculo = texto.lower()


print(f" o texto em letra  maiusculo :{texto_minusculo}")

# invertendo a posição da string

texto_invetido = texto[::-1]

print(f'streng invertida : {texto_invetido}')