import os
os.system("cls")

numero = int(input("digite um numero :"))



if (numero >= 20):
    print(f"numero maior {numero},Aprovado com sucesso !")

elif(numero ==20 ):
    print(f"numero igual {numero},Aprovado com sucesso !")

elif(numero < 20 ):
    print(f"numero menor {numero},Reprovado com sucesso!")

else:
    print(f"numero menor {numero}, valor invalido!")