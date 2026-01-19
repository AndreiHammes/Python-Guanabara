# Crie um programa que leia o nome e o valor de vários produtos. O programa deverá pserguntar se o usuário vai continuar no final. Mostre:
# - Qual é o total gasto na compra
# - Quantos produtos custam mais de 1000 reais
# - Qual o nome do produto mais barato

valor_total = 0
produto_mil = 0
valores = []

while True:
    produto = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    valor_total += valor
    valores.append(valor)
    barato = min(valores)
    if valor > 1000:
        produto_mil += 1
    escolha = input('Você quer continuar? [S/N] ').upper()
    if escolha == 'S':
        continue
    break
print(f'O valor total gasto na compra foi de R${valor_total:.2f}')
print(f'Você possui {produto_mil} produtos que custam mais de R$1000.00')
print(f'O nome do produto mais barato é: {barato:.2f}')
