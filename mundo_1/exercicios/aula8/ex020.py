# O mesmo professor do exercicio anterior quer sortear a ordem de apresentação de trabalho dos alunos
# Faça um programa que lei o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

nomes = [aluno1, aluno2, aluno3, aluno4]
shuffle(nomes)

print(f'A ordem escolhida foi : {nomes}')