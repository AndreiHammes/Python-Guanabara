# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

import random


aleatorio = tuple(random.randint(0,26) for i in range(5))
print(f"Listagem --> {aleatorio}")
print(f'O menor valor é {min(aleatorio)} e o maior é {max(aleatorio)}')
