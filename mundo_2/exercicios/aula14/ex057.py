# Faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
    
sexo = input('Digite o sexo da pessoa: ')
while sexo not in 'MmFf':
    sexo = input('Valor inválido, digite um valor válido: ')
print(f'Sexo {sexo} registrado!')