# Crie um programa que exiba na tela todos os números pares no intervalo entre 1 e 50

lista_pares = []
for i in range(1,50):
    if i % 2 == 0:
        lista_pares.append(i)

print(lista_pares)