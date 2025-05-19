# Mostre um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário: '))
valor_aumento = salario + ((15 * 100) / 2)
print(f'O salário ajustado é :{valor_aumento:.2f}')