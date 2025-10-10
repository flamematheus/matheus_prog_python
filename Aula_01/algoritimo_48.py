import os
os.system("cls")

salariominimo =float(input("digite o salario minimo:"))
quilowatts =float(input("digite a quantidade de quilowattes consumida : "))


valor_por_quilowatt = (salariominimo/7)/100
valor_a_pagar = quilowatts*valor_por_quilowatt
valor_com_desconto = valor_a_pagar-(valor_a_pagar*0.10)

print(F"valor por quilowatts : {quilowatts:.2f}")
print(F"valor a ser pago :R$ {valor_a_pagar:.2f}")
print(F"valor com desconto :R$ {valor_com_desconto:.2f}")