# EXERCÍCIOS DE FIXAÇÃO
# Kwargs

# 2 - Crie uma função chamada 'combinar_dicionarios', que aceite dois ou mais dicionários como argumentos nomeados e retorne 
    # um único dicionário que combine todas as chaves e valores.

    # Input:
    # combinar_dicionarios(
    #     d1 = {'a': 1, 'b': 2},
    #     d2 = {'b': 3, 'c': 4},
    #     d3 = {'d': 5}
    # )

    # Resultado esperado:
    # {'a': 1, 'b': 3, 'c': 4, 'd': 5}

# ERRO? Verificar se o enunciado está correto, pois o resultado esperado parece não bater com o input ('b': 3 e 'b': 2).

def combinar_dicionarios(**kwargs):
    dicionario_combinado = {}

    for dicionario in kwargs:
        for chave, valor in dicionario:
            dicionario_combinado[chave] = valor

    return dicionario_combinado

print(combinar_dicionarios(d1 = {'a': 1, 'b': 2}, d2 = {'b': 3, 'c': 4}, d3 = {'d': 5}))
