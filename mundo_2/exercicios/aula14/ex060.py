# faça um programa que leia um número qualquer e mostre seu fatorial
# ex: 5! = 5x4x3x2x1 = 120

numero = int(input('Digite um número inteiro: '))

count = 1

for i in range(1, numero + 1):
    count  *= i

print(f'O resultado de {numero}! é: {count}')