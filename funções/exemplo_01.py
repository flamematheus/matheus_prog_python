import os
os.system ("cls")

def somar ():
    a = int(input("digite um numero:"))
    b = int(input("digite um numero:"))

    total = a + b
    print(total) 

def somar (A,B):
    total = A+B
    print(total) 
#-------------------------------------------#
print("função somar sem parametros")
#somar()

print("função somar com parametros")
num_01 =int(input("digite um numero:"))
num_02 =int(input("digite um numero:"))

somar (num_01,num_02)


