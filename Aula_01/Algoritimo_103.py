import os
os.system("cls")

ano = int(input("digite o ano do seu nascimento :"))
ano_atual = int(input("digite o ano do seu nascimento :"))

if(ano_atual - ano != 0 and ano_atual - ano <= 100):
    idade = ano_atual -ano
    print(f"idade{idade}")
else:
    print("data invalida")
