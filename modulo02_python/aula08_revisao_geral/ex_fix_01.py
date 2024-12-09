# EXERCÍCIOS DE FIXAÇÃO

# 1 - Aplicando Descontos
    # Você tem uma lista de preços de produtos e quer aplicar um desconto de 10% em todos os produtos.
    # Utilize a função 'map' para aplicar o desconto.

lista_produtos = [10.75, 14.9, 22.15]

lista_produtos_desconto = list(map(lambda preco: round(preco * 0.9, 2), lista_produtos))

print(lista_produtos_desconto)


# 2:
def calcular_90_por_cento(numero: float):
    resultado = numero * 0.9
    resultado_arredondado = round(resultado, 2)
    return resultado_arredondado

pecos_reduzidos = list(map(calcular_90_por_cento, lista_produtos))

print(pecos_reduzidos)
