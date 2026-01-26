# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados de forma tabular

produtos = ("violao", 6000, "bateria", 3500, "violino", 9000, "piano", 25000) 

for i in range(0, len(produtos), 2):
    print(f"{produtos[i]:.<20} R$ {produtos[i+1]:>8.2f}")