# Crie um programa que faça o computador jogar jokenpo com você
from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''Suas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')