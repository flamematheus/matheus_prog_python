import os
os.system ("cls")

import time

valores = [ 1,3,5,7,9]

for  i in range(len(valores)):
    valores [i]*=2
    print(valores[i])
    time.sleep (0.5)
print(valores)