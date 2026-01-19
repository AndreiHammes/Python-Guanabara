# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado, e o programa vai informar quantas cédulas de cada valor serão entregues
# OBS - considere que o caixa possui cédulas de 50, 20, 10 e 1

print('Caixa Eletrônico')
valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
nota = 50
total_notas = 0
while True:
    if total >= nota:
        total -= nota
        total_notas += 1
    else:
        if total_notas > 0:
            print(f'Total de {total_notas} notas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota == 1
        total_notas = 0
        if total == 0:
                break
