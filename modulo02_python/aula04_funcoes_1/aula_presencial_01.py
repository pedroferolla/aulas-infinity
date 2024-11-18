# Fazer cálcula da área de imóveis:
# 1) 3 x 4
# 2) 19 x 13
# 3) 4 x 10

def calcular_area(altura: float, largura: float):
    area = altura * largura
    return area

# Exemplo antes da função:
# altura_1 = 3
# largura_1 = 4
# area_1 = altura_1 * largura_1
# print(f'Área 1: {area_1} m²')

altura_1 = 3
largura_1 = 4
area_1 = calcular_area(altura_1, largura_1)
print(f'Área 1: {area_1} m²')


# Exemplo antes da função:
# altura_2 = 3
# largura_2 = 4
# area_2 = altura_2 * largura_2
# print(f'Área 2: {area_2} m²')

area_2 = calcular_area(19, 13)
print(f'Área 2: {area_2} m²')



# Exemplo antes da função:
altura_3 = 3
largura_3 = 4
area_3 = altura_3 * largura_3
print(f'Área 3: {area_3} m²')
