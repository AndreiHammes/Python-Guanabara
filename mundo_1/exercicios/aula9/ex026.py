# Crie um programa que leia uma frase pelo teclado e mostre
# Quantas vezes aparece a letra 'a'
# Em que posição ela aparece a primeira vez
# em que posição ela aparece a última vez

frase = str(input('Digite a frase: ')).strip().lower()
print(f'A letra "a" aparece {frase.count("a")} vezes') 

print(f'A letra "a" aparece pela primeira vez na posição {frase.find("a")+1}')
print(f'A letra "a" aparece pela última vez na posição {frase.rfind("a")+1}')