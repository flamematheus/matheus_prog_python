import os
os.system("cls")

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))

resultado = (numero1 + numero2) /3

if(resultado > 0 ):
    print(F"resultado positivo :{resultado}")

elif (resultado < 0):

    print(F"resultado negativo:{resultado}.2f")
else :  
    print("resultado invalido")