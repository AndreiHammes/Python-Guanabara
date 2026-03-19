# Crie um programa que tenha uma tupla com várias palavaras (sem acentos). Depois disso, mostrar para cada palavra, quais são as suas vogais

palavras = ('casa', 'carro', 'moto', 'aviao', 'navio')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra in 'aeiouAEIOU':
            print(letra, end=' ')
