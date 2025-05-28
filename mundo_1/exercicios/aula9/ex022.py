# Crie um programa que leia o nome completo de uma pessoa e retorne:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todo sem contar espaços
# - quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Em maiúsculo: {nome.upper()}')
print(f'Em minúsculo: {nome.lower()}')
print(f'Total de letras: {len(nome)-nome.count(' ')}')
nome_separado = nome.split()
print(f'Seu primeiro nome é: {nome_separado[0]} e ele tem {len(nome_separado[0])} letras1')
