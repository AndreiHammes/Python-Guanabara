# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite seu nome: ')).strip().lower()
print('silva' in nome)
# o in não é um método e sim um operador
