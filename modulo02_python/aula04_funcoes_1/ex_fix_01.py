# EXERCÍCIOS DE FIXAÇÃO

# 1 - Crie uma função chamada 'area_retangulo' que receba dois parâmetros: 'largura' e 'altura'.
    # A função deve retornar a área do retângulo, que é calculada como 'largura * altura'.

    # Input:
        # largura = 4
        # altura = 3

    # Resultado esperado:
        # 12

def area_retangulo(largura: float, altura: float):
    area = largura * altura
    return area

# Resolução 1:
print(area_retangulo(4, 3))


# Resolução 2:
largura = 4
altura = 3
area_1 = area_retangulo(4, 3)
print(f'A área do retângulo é: {largura}m (largura) x {altura}m (altura) = {area_1}m².')
