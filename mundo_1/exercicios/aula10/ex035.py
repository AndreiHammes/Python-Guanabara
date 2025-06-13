# Desenvolva um progrmaa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if (reta1 + reta2) > reta3 and (reta3 + reta2) > reta1 and (reta1 + reta3) > reta2:
    print('O triãngulo pode ser montado!')
else:
    print('O triângulo não pode ser montado!')