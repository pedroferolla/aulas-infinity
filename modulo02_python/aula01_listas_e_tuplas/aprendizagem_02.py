# APRENDIZAGEM

# 2 - Remova os valores duplicados:
    # lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nova_lista = []

for i in lista:
    if i in nova_lista:
        continue
    nova_lista.append(i)

print(nova_lista)
