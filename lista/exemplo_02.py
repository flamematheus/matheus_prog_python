import os
os.system ("cls")


#criando as listas
frutas = ["maçã","laranja","uva","banana"]
numeros = [1,2,3,4,5,6]
mista = [1,"texto",3,14,True]

#remove sempre o ultimo elemento
frutas2 = frutas.pop()
print(frutas2)
print(frutas)


#remove sempre o ultimo elemento nomeando 
frutas.pop(1)
print(frutas)
