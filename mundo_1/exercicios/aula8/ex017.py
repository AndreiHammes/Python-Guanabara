# Faça um programa que leia o comprimento do cateto oposto e do cateto adjecente de um triangulo retangulo
# Calcule e mostre o comprimento da hipotenusa

from math import sqrt

cat_a = float(input('Digite o comprimento do cateto oposto: '))
cat_b = float(input('Digite o comprimento do cateto adjecente: '))

hipo = sqrt(cat_a ** 2 +  cat_b ** 2)
print(f'O comprimento da hipotenua é: {hipo:.2f}')