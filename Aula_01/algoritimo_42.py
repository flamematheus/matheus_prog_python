import os
os.system("cls")

import math

# Entrada do usuário
graus = float(input("Digite o ângulo em graus: "))

# Conversão para radianos
radianos = math.radians(graus)

# Cálculo das funções trigonométricas básicas
seno = math.sin(radianos)
cosseno = math.cos(radianos)

# Tratamento para tangente, secante, cossecante e cotangente
try:
    tangente = math.tan(radianos)
except:
    tangente = float('inf')  # ou pode usar None

# Evita divisão por zero
secante = 1 / cosseno if cosseno != 0 else float('inf')
cosecante = 1 / seno if seno != 0 else float('inf')
cotangente = 1 / tangente if tangente != 0 else float('inf')

# Impressão dos resultados
print(f"\nResultados para o ângulo de {graus}°:")
print(f"Seno      = {seno:.6f}")
print(f"Cosseno   = {cosseno:.6f}")
print(f"Tangente  = {tangente:.6f}")
print(f"Secante   = {secante:.6f}")
print(f"Cossecante= {cosecante:.6f}")
print(f"Cotangente= {cotangente:.6f}")
