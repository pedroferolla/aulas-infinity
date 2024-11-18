# APRENDIZAGEM

# 8 - Dada uma lista de números, crie uma nova lista com apenas os números que são múltiplos de 3 ou 5.

    # numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = []

for i in numeros:
    if i % 3 == 0 or i % 5 == 0:
        nova_lista.append(i)

print(nova_lista)
