dados_heroi = ['Ragnar', 43, 'humano', ['voar', 'soltar gelo']]

dados_heroi = {
    'nome': 'Ragnar',
    'idade': 43,
    'raça': 'humano',
    'habilidades': ['voar', 'soltar gelo']
}

dados_heroi['raça']
dados_heroi[2]

lista_herois = [dados_heroi]

print(dados_heroi['habilidades'[1]])

print(f"Antes de mudar o valor: {dados_heroi['idade']}")

dados_heroi['idade'] = 44

print(f"Depois de mudar o valor: {dados_heroi['idade']}")


dados_heroi['gênero'] = 'Masculino'
del dados_heroi['nome']
print(dados_heroi)
