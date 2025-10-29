import os
os.system ("cls")

lista =[]

for i in range (51):
    lista.append(i)

#print(F"lista do exemplo  01 {lista}")


for i in range (51):
    if(i%2 != 0):
        lista.append(i)

print(F"lista do exemplo  02 {lista}")