# Aluguel de carros
# Escreva um programa que pergunte a quantidade de KM percorridos por um carro e a quantidade de dias que ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 0,15 reais por km rodado

km = float(input('Quantos Kms você percorreu com o carro? '))
dias = int(input('Por quantos dias você alugou o carro? '))

preco = (60 * dias) + (0.15 * km)

print(f'O preço final a se pagar é de: {preco:.2f}') 