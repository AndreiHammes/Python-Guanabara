# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o preço do produto: '))
desc = preco - ((5 / 100) * preco)
print(f'O preço do produto com o desconto de 5% aplicado é: {desc:.2f}')