# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# a vista dinheiro/cheque = 10% de desconto
# a vista no cartão = 5% de desconto
# em até 3x no cartão = preço normal
# 3x ou mais no cartão = 20% de juros

valor = float(input('Digite o valor do produto: '))

print('Ecolha um método de pagamento: ')
print('1 - A vista em dinheiro/cheque')
print('2 - A vista no cartão')
print('3 - Em até 3x no cartão')
print('4 - 3x ou mais no cartão')

escolha = int(input('Digite a opção desejada: '))

if escolha == 1:
    print(f'O valor do produto ficou em {valor - ((valor * 10) / 100)}')
elif escolha == 2:
    print(f'O valor do produto ficou em {valor - ((valor * 5) / 100)}')
elif escolha == 3:
    print(f'O valor do produto ficou em {valor} ')
elif escolha == 4:
    parcelas = int(input('Em quantas parcelas?'))
    if parcelas < 3:
        print('A quantidade mínima de parcelas é 3x no cartão')
    else:
        print(f'O valor do produto, em {parcelas} parcleas, ficou em {valor + ((valor * 20) / 100) / parcelas}')
else: 
    print('Opção inválida, tente novamente')