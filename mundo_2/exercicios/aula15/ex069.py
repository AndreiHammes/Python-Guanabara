# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuario quer ou não continuar, no final mostre:
# - Quantas pessoas tem mais de 18 anos
# - Quantoss homens foram cadastrados
# - Quantas mulheres com menos de 20 anos 

print('CADASTRE UMA PESSOA')

pessoa = 0
homens = 0
mulheres = 0

while True:
    idade = int(input('Digite a idade: '))
    if idade > 18:
        pessoa += 1
    sexo = input('Digite o sexo: [M/F] ').upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    escolha = input('Quer continuar? [S/N] ').upper()

    if escolha == 'S':
        continue
    break

print(f'''
Você cadastrou {pessoa} pessoas com mais de 18 anos
Você cadastrou {homens} homens
Você cadastrou {mulheres} mulheres com menos de 20 anos
      ''')