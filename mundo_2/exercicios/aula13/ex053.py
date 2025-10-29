# crie um programa que leia uma frase qualquer e diga se ela é um palindromo
# desconsiderando os espaços

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
juncao = ''.join.split()
inverso = ''
for letra in range(len(juncao) - 1, -1, -1):
    inverso += juncao(letra)

if inverso == juncao:
    print('Temos um palíndromo')
else:
    print('A frase não é um palíndromo')