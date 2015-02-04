#!/usr/bin/python3
#Escreva um programa que leia a quantidade de dias,
#horas, minutos e segundos do usuário. Calcule o total em segundos.

s_dia = 86400
s_horas = 3600
s_minutos = 60

dia = int(input("Dia(s): "))
horas = int(input("Hora(s): "))
minutos = int(input("Minuto(s): "))

em_segundos = (dia * s_dia) + (horas * s_horas) + (minutos * s_minutos)
print("Total: %d em segundos. " %em_segundos)
