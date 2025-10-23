# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, e mostre:
# a média de idade do grupo
# qual é o nome do HOMEM mais velho
# quantas mulheres tem menos de 20 anos

idades = []
nomes = []
sexo_m = []
sexo_f = []
count = 0
count_feminino = 0
count_masculino = 0
velho = ''

for i in range(1,5):
    print(f'----- {i}a pessoa -----')
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: [M/F] ')


    if sexo == 'F' and idade < 20:
        sexo_f.append(sexo)
        count_feminino +=1 
    else:
        sexo_m.append(sexo)
        count_masculino += 1

        idades.append(idade)
        count += idade

media = count / 4

print(f'A media das idades é: {media:.2f} ')
print(f'A idade da pessoa mais velha é: {max(idades)} e se chama {velho}')
print(f'Ao todo são {count_feminino} mulheres com menos de 20 anos')