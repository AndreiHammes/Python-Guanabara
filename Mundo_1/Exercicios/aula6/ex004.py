# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitido e todas as informações possíveis sobre ele

valor = input('Digite algo: ')
print(f'O tipo primitido desse valor é {type(valor)}:')
print(f'O valor {valor} tem somente espaços? ', valor.isspace())
print(f'O valor {valor} tem somente números? ', valor.isnumeric())
print(f'O valor {valor} tem somente letras? ', valor.isalpha())
print(f'O valor {valor} é alfanumérico? ', valor.isalnum())
print(f'O valor {valor} está em maiúsculo? ',valor.isupper())
print(f'O valor {valor} está em minúsculo? ', valor.islower())
print(f'O valor {valor} está capitalizado? ', valor.istitle())

# Esses métodos atribuidos ao nosso objeto "valor" podem identificar as características do objeto String