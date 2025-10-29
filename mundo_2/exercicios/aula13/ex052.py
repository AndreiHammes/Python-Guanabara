# Faça um programa que leia um número e diga se ele é ou não um número primo, ou seja que são diviseis apenas por 1 e por ele mesmo

numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero):
    if numero % c == 0:
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(f'{c}, ', end='')
print(f'\n\033[mO número {c} foi divisível {total} vezes')
if total == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
