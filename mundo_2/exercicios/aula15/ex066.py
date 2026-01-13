# Crie um programa que leia vários números inteiros pelo teclado
# o programa só vai parar quando o usuário digitar o valor 999 que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles 

numeros_digitados = soma_numeros = 0

while True:
    numero = int(input('Digite um número inteiro (999 para parar): '))
    if numero == 999:
        break
    numeros_digitados = numeros_digitados + 1
    soma_numeros += numero
    
print(f'Você digitou {numeros_digitados} números, e a soma total deles é {soma_numeros}')