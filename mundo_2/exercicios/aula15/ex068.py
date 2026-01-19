# Faça um programa que jogue par ou ímpar com o computador. O jogo só sera interrompido quando o jogador PERDER. Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

numeros = [1,2,3,4,5,6,7,8,9,10]
vitorias = 0

import random
valor_computador = random.choice(numeros)

print('VAMOS JOGAR PAR OU ÍMPAR!')

while True:
    valor = int(input('Digite um valor: '))
    escolha = input('Par ou ímpar? [P/I] ').upper()
    print(f'Você jogou {valor} e o computador {valor_computador}')

    total = valor + valor_computador

    if (total) % 2 == 0 and escolha == 'P':    
        print(f'total de {total} deu PAR, VOCÊ GANHOU!')
        vitorias += 1
    elif (total) % 2 == 0 and escolha == 'I':
        print(f'total de {total} deu PAR, VOCÊ PERDEU')
        break
    elif (total) % 2 == 1 and escolha == 'P':    
        print(f'total de {total} deu ÍMPAR, VOCÊ PERDEU!')
        break
    elif (total) % 2 == 1 and escolha == 'I':
        print(f'total de {total} deu ÍMPAR, VOCÊ GANHOU')
        vitorias += 1
    
print(f'GAME OVER, você ganhou {vitorias} vezes')