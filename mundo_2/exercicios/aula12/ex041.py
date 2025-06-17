# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
# de acordo com a idade:
# Até 9 anos : MIRIM
# até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

nascimento = int(input('Digite o ano do seu nascimeto: '))
idade = 2025 - nascimento

print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Categoria Mirim')
elif idade > 9 and idade <= 14:
    print('Categoria infantil')
elif idade > 14 and idade <= 19:
    print('Categoria Junior')
elif idade > 19 and idade <= 25:
    print('Categoria Senior')
else: 
    print('Categoria Master')