# Escreva um programa que faça o computador "pensar" em um número intreiro entre 0 e 5
# Peça para o usuário tentar adivinhar qual foi o número escolhido pelo computador
# O programa deverá exibir da tela se o usuário venceu ou perdeu

import random

numero = [0, 1, 2, 3, 4, 5]
n = random.choice(numero)

chute = int(input(f'Tente adivinhar o número de 1 a 5: '))
if chute == n:
    print('Você ganhou!')
else: 
    print('Você perdeu!')