# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 ate 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida 

peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')