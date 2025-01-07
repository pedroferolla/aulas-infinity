# ATIVIDADE PRÁTICA 1

# Dada uma lista de números, crie uma nova lista contendo apenas os números pares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nova_lista = []

for numero in lista:
    if numero % 2 == 0:
        nova_lista.append(numero)

print(nova_lista)
