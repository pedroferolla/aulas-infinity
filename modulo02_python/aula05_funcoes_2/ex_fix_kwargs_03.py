# EXERCÍCIOS DE FIXAÇÃO
# Kwargs

# 3 - Crie uma função chamada 'filtrar_valores', que aceite um número variável de argumentos nomeados e retorne um dicionário 
    # contendo apenas os pares chave - valor, onde o valor é um número maior que 10.

    # Input:
    # filtrar_valores(a = 5, b = 20, c = 15, d = 8)

    # Resultado esperado:
    # {'b': 20, 'c': 15}

def filtrar_valores(**kwargs):
    valores_filtrados = {}

    for chave, valor in kwargs.items():
        if valor > 10:
            valores_filtrados[chave] = valor

    return valores_filtrados

print(filtrar_valores(a = 5, b = 20, c = 15, d = 8))
