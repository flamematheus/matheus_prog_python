import os
os.system("cls")

pessoa = {
    "nome":"joão",
    "idade":30,
    "cidade":"São Paulo",
    "email":"batabaa@email.com",

}

pessoa ["nome"]="Paulo"
print(pessoa)

#Updade e para atualizar os valores 
pessoa.update({"estado":"sp"})
print(pessoa)

pessoa.update({"endereço":"rua java ali,74", "CEP":"08963-500"})
print(pessoa)


pessoa.pop("email")
print(pessoa)
#remover o ultimo item do dicionario 
pessoa.popitem()
print(pessoa)

#deleta o dado da base 
del pessoa["endereço"]
print(pessoa)


#limpa todos os dados das  pessoas 
pessoa.clear()
print(pessoa)

print(len(pessoa))
