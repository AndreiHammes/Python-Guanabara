# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de futebol, na ordem de colocação. Depois mostre:
# apenas os 5 primeiros colacados
# os últimos 4 colocados da tablea
# uma lista com os times em ordem alfabética
# em que posição na tabela está o time da Chapecoense

colocados_brasileirao = (
    "Palmeiras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo", 
    "Bragantino", "Fluminense", "Athletico-PR", "Internacional", "Fortaleza", 
    "São Paulo", "Cuiabá", "Corinthians", "Cruzeiro", "Vasco", 
    "Bahia", "Santos", "Goiás", "Coritiba", "América-MG"
)

print(f'\nOs 5 primeiros colocados são: {colocados_brasileirao[:5]}')
print(f'\nOs 4 últimos colocados da tabela são: {colocados_brasileirao[-4:]}')
print(f'\nA lista com os times em ordem alfabética fica: {sorted(colocados_brasileirao)}\n')