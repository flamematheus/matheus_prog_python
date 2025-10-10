import os
os.system('cls')

dividendo = int(input("Digite um numero: "))
divisor = int(input("Digite um numero: "))

quociente = dividendo/divisor
resto = dividendo%divisor

print("Dividendo: ",dividendo)
print("Divisor: ",divisor)
print("Quociente: ",quociente)
print("Resto: ",resto)