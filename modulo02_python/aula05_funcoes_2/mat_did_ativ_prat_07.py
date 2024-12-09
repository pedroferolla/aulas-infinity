# ATIVIDADE PRÁTICA 7

# Crie uma função chamada 'criar_lista_de_compras', que aceita um número variável de itens de compras como argumentos 
# posicionais (usando *args).
# A função deve criar e retornar uma lista de compras que contenha todos os itens fornecidos.

def criar_lista_de_compras(*args):
    lista_de_compras = []
    lista_de_compras.append(args)
    return lista_de_compras

print(criar_lista_de_compras('Imbel GC MD2 .380', 'CZ P10-F 9mm', 'Benelli M4 Tactical', 'Imbel GC MD7 .45'))
