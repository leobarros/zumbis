#!/usr/bin/python3
#04-02-15

#Escreva um programa que leia um valor
#em metros e o exiba convertido em milímetros

valor = float(input('Informe o valor em metros: '))
mm_valor = (valor * 1000.0)

print('Valor em milimetros: %.2f' %mm_valor)
