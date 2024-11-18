dados_heroi = ['Ragnar', 43, 'humano', ['voar', 'soltar gelo']]

dados_heroi = {
    'nome': 'Ragnar',
    'idade': 43,
    'raça': 'humano',
    'habilidades': ['voar', 'soltar gelo']
}

# ITEM = CHAVE + VALOR

# Imprimir chaves do dicionário:
for chave in dados_heroi:
    print(chave)


# Imprimir valores do dicionário:
for valor in dados_heroi.values():
    print(valor)

# Imprimir itens do dicionário:
# ".items" cria tuplas:
for item in dados_heroi.items():
    print(item)

# Desmembrando as tuplas criadas pelo ".items":
for chave, valor in dados_heroi.items():
    print(f'A chave {chave} tem o valor {valor}')
