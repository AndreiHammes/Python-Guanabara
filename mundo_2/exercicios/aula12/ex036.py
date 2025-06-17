# Escreva un progrma para aprovar o empréstimo bancário para a compra de uma casa
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

print('Vamos conferir a possibilidade do seu empréstimo!')

valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o valor do seu salário: R$ '))
anos = int(input('Digite em quantos anos você vai pagar: '))

total_meses = anos * 12
prestacao_mensal = valor_casa / total_meses
limite_salario = salario * 0.30

if prestacao_mensal <= limite_salario:
    print('Empréstimo aceito!')
else:
    print('Empréstimo negado, o valor da mensalidade excede o permitido!')