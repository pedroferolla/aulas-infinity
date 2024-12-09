# EXERCÍCIOS DE FIXAÇÃO
# Args

# 8 - Crie uma função chamada 'agrupar_listas', que aceite um número variável de listas como argumentos e retorne uma única 
    # lista contendo todos os elementos das listas fornecidas.

    # Input:
    # agrupar_listas([1, 2], [3, 4], [5, 6])

    # Resultado esperado:
    # [1, 2, 3, 4, 5, 6]

def agrupar_listas(*args):
    listas_agrupadas = []

    for lista in args:
        for item in lista:
            listas_agrupadas.append(item)

    return listas_agrupadas

print(agrupar_listas([1, 2], [3, 4], [5, 6]))
