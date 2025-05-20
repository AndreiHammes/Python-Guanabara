# importando uma módulo completo --> import bebidas
# importando uma parte do módulo --> from doce import pudim

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc

num = float(input('Digite um número real: '))
print(f'A parte inteira de {num} é: ', trunc(num))
