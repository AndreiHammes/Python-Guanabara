# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista. Já na posição correta de inserção(sem usar o sort())
# No final mostre a lista ordenada na tela

numeros = []


for i in range(1,6):
    valor = int(input(f'Digite o {i} valor: '))
    numeros.append(valor)
    if valor >= 0:
        print(f'Valor adicionado ao final da lista...')




