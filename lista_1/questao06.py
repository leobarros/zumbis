#!/usr/bin/python3

'''
Calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média
esperada para a viagem
Base da fórmula:
http://www.sofisica.com.br/conteudos/Mecanica/Cinematica/velocidade.php
'''

distancia = float(input("Qual é a distância: "))
velocidade_media = float(input("Velocidade Média: "))

tempo = (distancia /velocidade_media)


print("O tempo de viagem é de: ", tempo)
