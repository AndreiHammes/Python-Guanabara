# Crie um programa que vai ler vários números e adicionar em uma lista
# Depois disso, mostre:
# - Quantos números foram digitados
# - A lista de valores, ordenada de forma decrescente
# - Se o valor 5 foi digitado e está ou não na lista

lista = []

while True:
    valor = int(input('Digite um valor: '))

    lista.append(valor)

    escolha = input('Quer continuar? [S/N] ').upper()

    if escolha == 'S':
        continue
    else:
        break

print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')

if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não apareceu na lista!')