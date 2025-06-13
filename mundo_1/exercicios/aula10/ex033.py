# Faça um programa que leia 3 números e motre qual é o maior e qual é o menor

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n2 > n3:
    print('O primeiro número é o maior!')
elif n2 > n1 and n1 > n3:
    print('O segundo número é o maior!')
else: 
    print('O terceiro número é o maior!')