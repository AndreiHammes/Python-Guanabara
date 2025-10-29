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


for i in range(1,5):
    print(f'----- {i}a pessoa -----')
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: [M/F] ')

    for i in nome:
        nomes.append(nome)

    if sexo in 'Ff' and idade < 20:
        sexo_f.append(sexo)
        count_feminino +=1 
    else:
        sexo_m.append(sexo)
        count_masculino += 1

        idades.append(idade)
        count += idade


media = count / 4
mais_velho = max(idades)
indice_mais_velho = idades.index(mais_velho)
nome_mais_velho = nomes[indice_mais_velho]

print(f'A media das idades é: {media:.2f} ')
print(f'A idade do homem mais velho é {mais_velho} e ele se chama {nome_mais_velho}')
print(f'Ao todo são {count_feminino} mulheres com menos de 20 anos')