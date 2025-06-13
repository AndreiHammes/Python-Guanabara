# Desenvolva um programa que pergunte a distância de uma viagem em KM. 
# Calcule o preço da passagem, cobrando 0,50 por KM para viagens até 200km e 0.45 para viagens mais longas

distancia = float(input('Qual a distância da viagem em KM? '))
if distancia <= 200:
    print(f'O preço da passagem é de: {distancia * 0.50}')
else:
    print(f'O preço da passagem é de: {distancia * 0.45}')