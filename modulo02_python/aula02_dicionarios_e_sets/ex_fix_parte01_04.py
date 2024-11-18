# EXERCÍCIOS DE FIXAÇÃO - PARTE 1/2

# Dado o dicionário "produto" com as seguintes chaves e valores:
    # "nome": "Laptop"
    # "preço": 3500
    # "quantidade": 10

# Remova a chave "quantidade" do dicionário.
# Imprima o dicionário após a remoção, mostrando as chaves restantes e seus valores.

produto = {
    'nome': 'Laptop',
    'preço': 3500,
    'quantidade': 10
}

del produto['quantidade']

print(produto)
