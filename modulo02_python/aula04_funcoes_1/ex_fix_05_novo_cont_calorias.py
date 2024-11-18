# EXERCÍCIOS DE FIXAÇÃO

# 5 - Contador de Calorias em uma Refeição
    # Problema: você quer controlar as calorias ingeridas durante o dia. Crie uma função que calcule o total de calorias 
    # de uma refeição, considerando que a função recebe uma lista de alimentos consumidos e o número de calorias de 
    # cada um.

    # Exemplo de entrada:
    # Alimentos: ['arroz', 'feijão', 'carne']
    # Calorias por alimento: [150, 100, 200]

    # Exemplo de saída:
    # Total de calorias: 450

calorias_por_alimento = [150, 100, 200]

def total_calorias(calorias_por_alimento):
    calorias_totais = 0
    for caloria in calorias_por_alimento:
        calorias_totais += caloria

    return calorias_totais

print(f'\nTotal de calorias: {total_calorias(calorias_por_alimento)}')
