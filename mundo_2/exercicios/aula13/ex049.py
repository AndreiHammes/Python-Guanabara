# refaça o ex09 mostrando a tabuada de um número que o usuário escolher só que agora utilizando o laço for

# ex09 - Faça um prorgama que leia um número inteiro qualquer e mostre na tela a sua tabuada


numero = int(input('Digite um número inteiro: '))
print('-' * 11)

for i in range(1,10):
    print(f'{numero} x {i} = {numero * {i}}')

print('-' * 11)
