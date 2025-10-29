# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, e mostre:
# a média de idade do grupo
# qual é o nome do HOMEM mais velho
# quantas mulheres tem menos de 20 anos

idades = []
nomes = []
soma_idades = 0 
mulheres_jovens = 0 
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''

for i in range(1, 5): 
    print(f'----- {i}ª pessoa -----')
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: [M/F] ')

    soma_idades += idade

    if sexo in 'Ff':
        if idade < 20:
            mulheres_jovens += 1
    
    elif sexo in 'Mm':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome


media = soma_idades / 4

print(f'\nA média das idades é: {media:.2f}')

if nome_homem_mais_velho:
    print(f'O nome do homem mais velho é {nome_homem_mais_velho} com {idade_homem_mais_velho} anos.')
else:
    print('Não foi informado nenhum homem na lista.')
    
print(f'Ao todo são {mulheres_jovens} mulheres com menos de 20 anos.')