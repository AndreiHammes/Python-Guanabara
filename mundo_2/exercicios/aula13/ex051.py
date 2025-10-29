# Desenvolva um programa que leia o primeiro termo e a razão de uma PA
# no final mostre os 10 primeiros termos dessa progressão

termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for c in range(1,11):
    termo_atual = termo + (c - 1) * razao

    print(f'{c}º Termo: {termo_atual}')