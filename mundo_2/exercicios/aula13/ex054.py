# crie um programa que leia o ano de nascimento de sete pesoas
# no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
# considere a maioridade como 21 anos

maioridade = 0
menores = 0
for c in range(1,8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = 2025 - ano_nascimento
    
    if idade >= 21:
        maioridade += 1
    else:
        menores += 1

print(f'Temos {maioridade} pessoas maiores de idade e {menores} pessoas menores de idade')