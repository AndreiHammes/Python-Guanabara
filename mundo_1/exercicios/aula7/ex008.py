# Escreva um programa que leia um valor em metros e escreva ele convertido em centímetros e milímetros

valor = float(input('Digite um valor em metros: '))
print(
    f'O valor {valor}M em:'
    f'\n- Centímetros: {valor * 100}Cm'
    f'\n- Milímetros: {valor * 1000}Mm'
)

# Desafio extra proposto: Informe também a medida em quilometros, hectometros, decametros e decimetros

print(
    f'O valor {valor} em:'
    f'\n- Quilômetros: {valor / 1000:.2f} km'
    f'\n- Hectômetros: {valor / 100:.2f} hm'
    f'\n- Decâmetros: {valor / 10:.2f} dam'
    f'\n- Decímetros: {valor * 10:.2f} dm'
)