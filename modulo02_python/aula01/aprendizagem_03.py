# APRENDIZAGEM

# 3 - Crie uma lista contendo os quadrados de cada número, de 1 a 10.

lista = []

for i in range(1, 11):
    i *= i
    lista.append(i)

print(lista)
