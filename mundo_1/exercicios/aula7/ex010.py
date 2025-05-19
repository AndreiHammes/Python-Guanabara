# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

valor_carteira = float(input('Digite quanto você tem na sua carteira: R$'))
dolar = valor_carteira / 5.64
print(f'Você pode comprar US{dolar:.2f} dólares!')