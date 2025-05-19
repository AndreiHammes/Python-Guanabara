# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o preço do produto: '))
desc = preco - (preco * 5 / 100)
print(f'O preço do produto com o desconto de 5% aplicado é: {desc:.2f}')

# A fórmula para calcular a porcentagem é multiplicar o valor que desejamos aplicar o desconto pela porcentagem desejada (no caso 5) 
# e dividir esse valor por 100