# faça um programa que leia o peso de 5 pessoas
# e no final, mostre qual foi o maior e o menor peso lido

pesos = []

def valor_invalido():
    print('Valor inválido!')

def pegar_pesos():
    try:
        for c in range(1,6):
            peso = float(input('Digite seu peso: '))
            pesos.append(peso)
    except:
        valor_invalido()
        


def exibir_menor_maior_peso():
    print(f'O menor peso é: {min(pesos)}kg')
    print(f'O maior peso é: {max(pesos)}kg')


pegar_pesos()
exibir_menor_maior_peso()