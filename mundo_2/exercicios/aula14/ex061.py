# refaça o desafio 51 lendo o primeiro termo e a razão de uma progressão aritmética, mostrando os 10 primeiros termos
# da progressão usando a estrutura while

# código desenvolvido no desafio 51:

# termo = int(input('Digite o termo da PA: '))
# razao = int(input('Digite a razão da PA: '))

# for c in range(1,11):
#     termo_atual = termo + (c - 1) * razao

#     print(f'{c}º Termo: {termo_atual}')

termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))

count = 1
termo_atual = 0

while count <= 10:
    termo_atual = termo + (count - 1) * razao
    print(f'{count}º termo: {termo_atual}')    
    count += 1