# faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 
# e que se encontram no intervalo de 1 até 500
soma = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            soma += c
print(f'A soma de todos os números ímpares no intervalo de 1 até 500 é: {soma}')