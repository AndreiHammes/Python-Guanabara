# Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo.
# Considere que 1 litro de tinta pinta uma área de 2m metros quadradaos

altura_parede = float(input('Digite a largura da parede: '))
largura_parede = float(input('Digite a largura da parede: '))

area = altura_parede * largura_parede

tinta = area / 2

print(f'Para pintar essa parede de área {area:.2f} você vai precisar de {tinta:.2f} litros de tinta!')