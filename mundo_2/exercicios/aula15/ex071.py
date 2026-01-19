# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado, e o programa vai informar quantas cédulas de cada valor serão entregues
# OBS - considere que o caixa possui cédulas de 50, 20, 10 e 1

cinquenta = 0


print('CAIXA ELETRÔNICO')

while True:
    valor = int(input('Qual será o valor a ser sacado? '))
    print(f'Para sacar R${valor}, você vai precisar de ')