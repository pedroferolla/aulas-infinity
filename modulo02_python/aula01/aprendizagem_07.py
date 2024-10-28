# APRENDIZAGEM

# 7 - Dada uma lista de listas, onde cada sublista contém dois números, crie uma nova lista com a soma dos 
    # números de cada sublista.

    # lista = [[1, 2], [3, 4], [5, 6]]

lista = [[1, 2], [3, 4], [5, 6]]

nova_lista = []

for sublista in lista:
    soma = 0
    novo_item = 0    

    for i in sublista:
        soma += i

    novo_item += soma

    nova_lista.append(novo_item)

print(nova_lista)
