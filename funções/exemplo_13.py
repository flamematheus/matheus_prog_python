import os
os.system("cls")

def dividir (a,b):
    quociente = a //b
    resto = a % b
    return quociente ,resto

q,r = dividir (10,3)
print(f"quociente:{q},resto : {r}")