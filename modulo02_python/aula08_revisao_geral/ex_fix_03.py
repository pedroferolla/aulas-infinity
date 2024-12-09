# EXERCÍCIOS DE FIXAÇÃO

# 3 - Filtrando Números Pares
    # Você tem uma lista de números e quer filtrar apenas os números pares.
    # Use a função 'filter' para fazer isso.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista_numeros_pares = list(filter(lambda numero: numero % 2 == 0, lista_numeros))

print(lista_numeros_pares)
