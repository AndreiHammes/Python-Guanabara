# Conversor de temperaturas
# Escreva um programa que converta uma temperatura digitada em graus celsius para Fahrenheit

temp = float(input('Digite a temperatura em °C: '))
fahren = (temp * 1.8) + 32
print(f'A temperattura de °C{temp} em Fahrenheit é: {fahren:.2f}°F')