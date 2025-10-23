import os
os.system ("cls")
import time

total =0
cont = 1
num =int(input("digite um numero:"))

while   (cont <=10):
    total = num *cont
    print(f"{num} X {cont} = {total}")
    time.sleep(0.5)
    cont +=1
