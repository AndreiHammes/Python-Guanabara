# Crie um programa que vai ler vários números e colocar em uma lista

# depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.

# ao final, moster o conteúdo das 3 listas geradas

# gerar primeiro os números e depois validar e passar para as de par ou impar

lista = []
par = []
impar = []

while True:
    valor = int(input('Digite um valor: '))

    lista.append(valor)

    escolha = input('Quer continuar? [S/N] ').upper()

    if escolha == 'S':
        continue
    elif escolha == 'N':
        break
    else:
        print('Digite um valor válido [S/N]')

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')