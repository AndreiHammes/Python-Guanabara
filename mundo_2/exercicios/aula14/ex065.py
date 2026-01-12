# crie um programa que leia varios números inteiros pelo teclado, no final da execução mostre a média entre todos os valores
# e qual foi o maior e o menor valor lido. o programa deve perguntar ao usuário se ele quer continuar digitando valores

numero = []
media = 0
quantidade = 0
soma_numeros = 0

while True:
    numeros = int(input('Digite um número inteiro (999 para parar): '))
    if numeros == 999:
        break
    numero.append(numeros)
    quantidade = quantidade + 1
    soma_numeros = sum(numero)
    media = soma_numeros / quantidade
    escolha = input('Você deseja continuar digitando valores? [S/N]').upper()
    if escolha == 'S':
        continue
    else:
        break


print(f"A média entre todos os valores é: {media}")
print(f'O maior valor lido foi {max(numero)} e o menor foi {min(numero)}')

