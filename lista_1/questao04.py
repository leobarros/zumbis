#!/usr/bin/python3

'''Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e do novo salário'''


salario = float(input("Salario: "))
per_salario = float(input("Quantos porcento de aumento?: "))
total_porcento = (salario * per_salario) / 100

print("Valor da porcentagem: ", total_porcento)
print("Valor total do salario: ", salario + total_porcento)
