# Escreva um programa que leia dois números inteiros e compare-os
# mostrando na tela a seguinte mensagem
# O primeiro valor é maior
# o segundo valor é maior
# não existe valor maior, os dois são iguais

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor1 > valor2:
    print('O primeiro valor é maior')
elif valor2 > valor1:
    print('O segundo valor é maior')
else: 
    print('Não existe valor maior, os dois são iguais')