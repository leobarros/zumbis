#!/usr/bin/python3

'''
Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
preço a pagar
'''

valor_mercadoria = float(input("Preço: "))
desconto = float(input("Desconto: "))
valor_real = valor_mercadoria - desconto

print("Desconto da mercadoria: ", desconto)
print("Total a pagar: ", valor_real)
