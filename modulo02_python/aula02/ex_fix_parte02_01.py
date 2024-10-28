# EXERCÍCIOS DE FIXAÇÃO - PARTE 2/2

# 1 - A partir do dicionário abaixo, adicione um novo livro e atualize o ano de publicação de um livro existente.
    # Exiba o dicionário atualizado:

biblioteca = {
    "1984": {"autor": "George Orwell", "ano": 1949},
    "O Senhor dos Anéis": {"autor": "J.R.R. Tolkien", "ano": 1954},
    "O Hobbit": {"autor": "J.R.R. Tolkien", "ano": 1937}
}

biblioteca['O Imbecil Coletivo'] = {'autor': 'Olavo de Carvalho', 'ano': 1996}

biblioteca['O Senhor dos Anéis']['ano'] = 2054

print(biblioteca)
