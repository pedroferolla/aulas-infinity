# EXPLORAÇÃO

# 1 - Calculadora de Tamanho de Roupas
    # Problema: você foi contratado para fazer um programa que descobre qual o tamanho de roupa que as mulheres devem 
    # comprar, com base nas suas medidas corporais.
    # Crie uma função que, dada a medida do busto, cintura e quadril, informe o tamanho da roupa (P, M ou G).

    # Tamanho    Busto                Cintura              Quadril
    # P          até 88 cm            até 68 cm            até 94 cm
    # M          89 - 94 cm           69 - 74 cm           95 - 100 cm
    # G          a partir de 95 cm    a partir de 75 cm    a partir de 101 cm

    # Exemplo 1:
    # Entrada:
    # Busto: 85 cm
    # Cintura: 65 cm
    # Quadril: 90 cm

    # Saída:
    # O tamanho recomendado é: P

    # Exemplo 2:
    # Entrada:
    # Busto: 92 cm
    # Cintura: 72 cm
    # Quadril: 98 cm

    # Saída:
    # O tamanho recomendado é: M

    # Exemplo 3:
    # Entrada:
    # Busto: 98 cm
    # Cintura: 80 cm
    # Quadril: 105 cm

    # Saída:
    # O tamanho recomendado é: G

def tamanho_recomendado(busto: int, cintura: int, quadril: int):
    if busto in range(89) and cintura in range(69) and quadril in range(95):
        recomendado = 'P'
        return recomendado
    elif busto in range(89, 95) and cintura in range(69, 75) and quadril in range(95, 101):
        recomendado = 'M'
        return recomendado
    elif busto >= 95 and cintura >= 75 and quadril >= 101:
        recomendado = 'G'
        return recomendado
    
recomendacao = tamanho_recomendado(busto = int(input('Busto (cm): ')), cintura = int(input('Cintura (cm): ')), quadril = int(input('Quadril (cm): ')))

print(f'\nO tamanho recomendado é: {recomendacao}')
