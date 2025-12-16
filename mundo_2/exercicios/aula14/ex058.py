# Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre o e 10
# só que agora o jogador vai tentar adivinhar até ele acertar, mostrando no final quantos palpites foram dados para acertar

import random

numero = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = random.choice(numero)

soma = 1

chute = int(input('Tente adivinhar o número de 0 a 10: '))

while chute != n:
    chute = int(input('Valor incorreto, tente outro número: '))
    n = random.choice(numero)
    soma += 1
print(f'Valor correto, você tentou {soma} vezes!')

# lógica alterada para ele escolher um número novo a cada iteração