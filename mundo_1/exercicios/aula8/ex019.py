# Um progrssor quer sortear um dos seus quatro alunos para apagar o quadro
# faça um programa que ajude ele, lendo o nome dos alunos e mostrando o nome escolhido

import random 

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

nomes = aluno1 + aluno2 + aluno3 + aluno4

sortear = random.shuffle(nomes)
print(sortear)