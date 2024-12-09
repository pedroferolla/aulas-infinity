def aumentar_preco(preco_antigo: float, porcentagem: int):
    '''
    Esta função adiciona uma porcentagem a um número.
    '''
    valor_porcentagem = 1 + (porcentagem / 100)
    preco_novo = preco_antigo * valor_porcentagem + 1
    return preco_novo

