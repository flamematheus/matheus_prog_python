import os
os.system ("cls")

import time

cont = 1
acm =  0

while (cont <= 10):
    acm += cont
    time.sleep(1.0)
    print(cont)
    cont += 1

print(f"total :{acm}")