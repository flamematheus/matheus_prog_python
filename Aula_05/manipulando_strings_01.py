import os
os.system("cls")

# função que remove os espaços em branco 
texto = " olá mundo com python"

print(texto.strip())

#função replace substitui uma string por outra
texto = "o Python e increvel !!!"
novo_texto = texto.replace(" python "," java ")
print(novo_texto)

#função split() devide a string em uma lista com base no delimitador
texto = "python , java , c#"
linguagem =texto.split(", ")
print(linguagem)

#função starswith() 
texto = "python é  incrivel !!"
print(texto.startswith("python")) 
print(texto.startswith("java")) 