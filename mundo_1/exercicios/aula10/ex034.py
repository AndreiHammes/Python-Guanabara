# Escreva um programa que pergunte o salário do funcionário e calcule o valor do seu aumento
# Para salários superiores a 1250, calcule um aumento de 10%
# para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Dgite o salário do funcionário: '))

if salario > 1250:
    print(f'O salário com aumento de 10% é de: {salario + (salario * 0.10)}')
else:
    print(f'O salário com aumento de 15% é de: {salario + (salario * 0.15)}')