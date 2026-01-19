# Faça um programa que mostre a tabuada de vários numeros, um de cada vez para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo

# Ex- Quer ver a tabuada de qual valor? > mostra a tabuada inteira dessa valor

while True:
    numero = int(input('Quer ver a tabuada de qual valor? (Digite um número negativo para sair) '))
    if numero < 0:
        break
    for i in range(1,11):
        print(f'{numero} X {i} = {numero * i}')