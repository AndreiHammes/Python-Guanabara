# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se já passou do tempo do alistamento
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo

nascimento = int(input('Digite o ano do seu nascimento: '))
idade = 2025 - nascimento

if idade < 18:
    print(f'Você ainda não precisa se alistar, ainda faltam {18 - idade} anos.')
elif idade == 18:
    print('Está na hora de você se alistar')
else:
    print(f'Já passou da época do seu alistamento, há cerca de {idade - 18} anos')