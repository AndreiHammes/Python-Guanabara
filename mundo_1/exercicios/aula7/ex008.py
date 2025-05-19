# Escreva um programa que leia um valor em metros e escreva ele convertido em centímetros e milímetros

valor = float(input('Digite um valor em metros: '))
print(f'O valor {valor}M possui {valor * 100}Cm e {valor * 1000}Mm')

# Desafio extra proposto: Informe também a medida em quilometros, hectometros, decametros e decimetros
print(f'O valor {valor} em Quilômetros é {valor / 1000}Km, o valor em hectometros é {valor / 100}Hm, o valor em decametros é {valor / 10}Dam e o valor em decímetros é {valor * 10}')