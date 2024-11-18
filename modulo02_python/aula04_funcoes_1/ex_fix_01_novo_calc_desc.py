# EXERCÍCIOS DE FIXAÇÃO

# 1 - Calculadora de Desconto
    # Crie uma função chamada 'calcular_desconto' que recebe o preço original de um produtoe e a porcentagem de desconto.
    # A função deve retornar o preço após aplicar o desconto.

    # Exemplo:
    # calcular_desconto(100, 15) deve retornar 85.0

def calcular_desconto(original):
    final = original * 0.85
    return final

print(calcular_desconto(200))
