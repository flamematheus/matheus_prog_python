import os
os.system("cls")


#Entrar com o nome de uma pessoa e só imprimi-lo se o prenome for JOSÉ

nome=str(input("digite seu nome :"))
pri_nome = nome.strip().split()[0]

if(pri_nome.upper()=="jose" ):
    print(F"seu segundo nome : : {pri_nome}")



else:
    print("nome invalido")




""""
nome_completo = input("Digite o nome completo: ")

# Separar o nome completo em partes
prenome = nome_completo.strip().split()[0]

# Verificar se o prenome é "JOSÉ"
if prenome.upper() == "JOSÉ":
    print(nome_completo)




"""