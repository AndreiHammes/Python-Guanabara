# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso  

numeros_extenso = ("um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

numero_escolha = int(input('Digite um número entre 1 e 20: '))
if numero_escolha >= 1 and numero_escolha <= 20:
    print(f"O número escolhido foi {numeros_extenso[numero_escolha - 1]}")
else:
    print('Tente novamente, digite somente um numero entre 1 e 20')

