# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares
# se o valor digitado for ímpar, desconsidere-o

soma = 0
for i in range(1,7):
    valor = int(input('Digite um número inteiro: '))
    if valor % 2 == 0:
        soma += valor    

print(soma)