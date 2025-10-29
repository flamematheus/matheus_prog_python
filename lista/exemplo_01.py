import os
os.system ("cls")


#criando as listas
frutas = ["maçã","laranja","uva","banana"]
numeros = [1,2,3,4,5,6]
mista = [1,"texto",3,14,True]

print(frutas[0])
print(frutas[-1])
print(frutas[1:3])

#imprimindo os elementos  na lista 
frutas.append("abacaxi")
print(frutas)


frutas.insert(2,"kiwui")
print(frutas)

numeros.append(7)
print(numeros)


numeros.insert(0,0)
print(numeros)
