#!/usr/bin/python3
# -*- coding: utf-8 -*-

quantidade_km = float(input("Quantos quilometros foram percorridos?: "))
quantidade_dia = int(input("Quantod dia de aleguel?: "))

carro_dia = 60.00
km = 0.15

valor_km = quantidade_km * km
valor_dia = quantidade_dia * carro_dia

print ("Total a pagar: ", valor_km + valor_dia)
