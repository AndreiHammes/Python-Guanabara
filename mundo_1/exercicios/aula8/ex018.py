# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

import math

angulo = float(input('Digite o angulo: '))

angulo_rad = math.radians(angulo)

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print(
    f'Os valores do ãngulo {angulo} são: \n'
    f'- Seno = {seno:.2f}\n'
    f'- Cosseno = {cosseno:.2f}\n'
    f'- Tangente = {tangente:.2f}'
)


