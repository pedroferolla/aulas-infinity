# APRENDIZAGEM

# 10 - Dada a lista de números inteiros abaixo, crie uma nova lista contendo apenas os números pares.

    # numeros = [2, 3, 4, 1, 5, 8, 7, 6, 10, 9]

numeros = [2, 3, 4, 1, 5, 8, 7, 6, 10, 9]
nova_lista = []

for i in numeros:
    if i % 2 == 0:
        nova_lista.append(i)

print(nova_lista)
