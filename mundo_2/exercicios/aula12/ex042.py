# Refaça o desafio 35 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo será formado
# Equilátero - todos os lados iguais
# isósceles - dois lados iguais
# Escaleno - Todos os lados diferentes

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if (reta1 + reta2) > reta3 and (reta3 + reta2) > reta1 and (reta1 + reta3) > reta2:
    print('As retas PODEM formar um triângulo!')
    if reta1 == reta2 and reta2 == reta3:
        print('E o triângulo formado será EQUILÁTERO (todos os lados iguais).')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('E o triângulo formado será ISÓSCELES (dois lados iguais).')
    else:
        print('E o triângulo formado será ESCALENO (todos os lados diferentes).')
else:
    print('As retas NÃO PODEM formar um triângulo.')

