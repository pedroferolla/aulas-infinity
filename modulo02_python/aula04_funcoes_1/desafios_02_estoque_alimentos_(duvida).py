# DESAFIOS:

# 2 - Verificação de Estoque de Alimentos do Supermercado
    # Problema: você está organizando a despensa de um mercado e precisa verificar se tem alimento suficiente.
    # Crie uma função que, dada uma lista de alimentos que você deseja e suas quantidades, e outra lista de alimentos 
    # disponíveis, retorne se todos os alimentos que você deseja estão disponíveis.

    # Exemplo de entrada:
    # Alimentos desejados: [['arroz', 2], ['feijão', 3]]
    # Alimentos no estoque: [['arroz', 3], ['feijão', 2], ['carne', 1]]

    # Exemplo de saída:
    # Faltam alimentos: [['feijão', 1]]

alimentos_estoque = [['arroz', 3], ['feijão', 2], ['carne', 1]]

alimentos_desejados = [['arroz', 2], ['feijão', 3]]

def verificar_estoque(alimentos_desejados: list):
    alimentos_faltantes = []
    
    if alimentos_desejados[0][0] in alimentos_estoque and alimentos_desejados[0][1] > alimentos_estoque[0][1]:
        alimento_0 = alimentos_estoque[0][1] - alimentos_desejados[0][1]
        alimentos_faltantes.append(alimentos_desejados[0][0], alimentos_desejados[0][alimento_0])

    if alimentos_desejados[1][0] in alimentos_estoque and alimentos_desejados[1][1] > alimentos_estoque[1][1]:
        alimento_1 = alimentos_estoque[1][1] - alimentos_desejados[1][1]
        alimentos_faltantes.append(alimentos_desejados[1][0], alimentos_desejados[1][alimento_1])

    return alimentos_faltantes

print(f'Faltam alimentos: {verificar_estoque(alimentos_desejados)}')
