# escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de Fibonnati

n = int(input('Digite quantos números você deseja visualizar da sequência de Fibonacci: '))
a,b = 0,1

fibonacci = []

for i in range(n):
    fibonacci.append(a)
    a,b = b, a + b
print(fibonacci)