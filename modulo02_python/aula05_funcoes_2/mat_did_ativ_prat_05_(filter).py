# ATIVIDADE PRÁTICA 5

# Crie uma função que aceita uma lista de números e use a função filter para retornar uma nova lista contendo apenas os 
# números pares da lista de entrada.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = list(filter(lambda numero: numero % 2 == 0, numeros))

print(numeros_pares)
