# Crie um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro e o último nome separadamente

nome = input('Digite seu nome completo: ').strip()
nome_completo = nome.split()
print(f'A primeira posição do nome é: {nome_completo[0]}')
print(f'A última posição do nome é: {nome_completo[-1]}')