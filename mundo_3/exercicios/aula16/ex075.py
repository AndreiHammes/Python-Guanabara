# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final. mostre:
# quantas vezes apareceu o valor 9
# em que posição foi digitado o primeiro valor 3
# quais são os números pares

cont = 0

numeros = (int(input('Digite o 1º número: ')),
           int(input('Digite o 2º número: ')),
           int(input('Digite o 3º número: ')),
           int(input('Digite o 4º número: ')))

print(f'O número 9 apareceu {numeros.count(9)} vezes')
     

if 3 in numeros:
    print(f'O primeiro número 3 apareceu na posição {numeros.index(3)+1}')

for i in numeros:
    if numeros.index(i) % 2 == 0:
        cont += 1
print(f"temos {cont} números pares")