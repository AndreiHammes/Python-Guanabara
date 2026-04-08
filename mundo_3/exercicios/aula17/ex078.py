# inserir elementos ao final da lista - append()
# Inserir elementes em um indice especifico - insert(indice, valor)
# deletar elementos - del nomedalista(indice) ou usamos o pop(), que podemos especificar o indice também. Normalmente o pop é para o último elemento, ou com o .remove(valor do elemento)

# podemos criar uma lista com um range inicial e final utilizando o operador list(range())

# .sort() para ordenar os valores, no inverso usamos o sort(reverse = True)
# len() para saber a quantidade de elementos em uma lista

# quando dizemos que b = a, estamos fazendo uma extensão do svalores e não copiando, se quisermos copiar usamos b = a[:]




# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista, no final mostre qual foi o maior e o menor valor digitado e as respectivas posições na lista

lista = []

for i in range(1,6):
    valores = input(f'Digite um valor par a posição {i}: ')
    lista.append(valores)

print(f'A lista ficou -> {lista}')
print(f'O maior valor foi {max(lista)} - na posição {lista.index(max(lista))}')
print(f'O menor valor foi {min(lista)} - na posição {lista.index(min(lista))}')

