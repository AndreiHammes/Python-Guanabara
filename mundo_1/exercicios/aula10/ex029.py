# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7 para cada KM acima do limite

velocidade = int(input('Qual é a velocidade do carro? '))
multa = velocidade - 80
valor = multa * 7

if velocidade > 80:
    print('Vocë foi multado!')
    print(f'O valor da multa é: {valor}')
else: 
    print('Você não foi multado')