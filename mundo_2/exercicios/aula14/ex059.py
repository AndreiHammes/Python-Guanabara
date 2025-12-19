# crie um programa que leia dois valores e mostre um menu na tela
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa
# seu programa deverá realizar a operação solicitada em cada caso

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

while True:
    print('''

        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do programa

          ''')
    valor = int(input('Escolha uma opção acima: '))

    if valor == 1:
        print(f"A soma entre {valor1} e {valor2} é {valor1 + valor2}")
    elif valor == 2:
        print(f"A multiplicação entre {valor1} e {valor2} é {valor1 * valor2}")
    elif valor == 3:
        if valor1 > valor2:
            print(f'{valor1} é maior que {valor2}')
        else:
            print(f'{valor2} é maior que {valor1}')
    elif valor == 4:
        print('Informe os números novamente:')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    else:
        break