# Faça um programa que leia um número e diga se ele é ou não um número primo, ou seja que são diviseis apenas por 1 e por ele mesmo

numero = int(input('Digite um número: '))

if numero % numero == 0 and numero % 1 == 0:
    print('é primo')
else:
    print('Não é primo')