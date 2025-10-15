import os
os.system("cls")

sigla = input("digite a sigla da cidade :")
uf = sigla.upper()

if (uf == "sp "):
    print("Paulista")

elif (uf == "MG"):
    print("mineiro")
    
elif (uf == "RJ"):
    print("Carioca")
else :
    print("outros estados")