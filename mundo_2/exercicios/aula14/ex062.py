# melhroe o exercicio 61, perguntando ao usuário se ele quer mostrar mais alguns termos
# o programa encerra quando o usuário digitar que quer 0 termos


termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))

count = 1
termo_atual = 0
total = 10

while True:
    for _ in range(total):
        termo_atual = termo + (count - 1) * razao
        print(f'{count}º termo: {termo_atual}')
        count += 1

    opcao = input('Quantos termos a mais? (0 para sair): ')
    if opcao.strip() == '0':
        break

    total = int(opcao) if opcao.strip().isdigit() else 0
    if total == 0:
        print('Entrada invalida, saindo...')
        break
    