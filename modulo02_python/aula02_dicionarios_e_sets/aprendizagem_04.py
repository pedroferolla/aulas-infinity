# APRENDIZAGEM

# 4 - Dado o dicionário 'contagem = {'a': 3, 'b': 5, 'c': 2}', escreva um loop que calcule e imprima a soma dos valores.

contagem = {'a': 3, 'b': 5, 'c': 2}

soma = 0

for valor in contagem.values():
    soma += valor

print(soma)
