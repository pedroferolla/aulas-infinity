# EXPLORAÇÃO

# 2 - Verificação de Data de Vencimento de Produtos
    # Problema: você comprou vários produtos e precisa saber se algum está vencido.
    # Crie uma função que, dada a data de vencimento de um produto e a data atual, verifique se o produto já venceu.

    # Exemplo de entrada:
    # Data de vencimento: 2024-10-30
    # Data atual: 2024-11-05

    # Exemplo de saída:
    # O produto está vencido.

    # DICA: o código abaixo está separando o ano, mês e dia da data abaixo:
    # data = '2024-05-30'
    # ano, mes, dia = data.split('-')

    # Como será que você pode colocar esse código para resolver o exercício?

data = '2024-05-30'
ano, mes, dia = data.split('-')

validade_produto = ''
data_atual = '2024-11-13'


data_hoje = {2024: {11: 13}}
data_vencimento = {}

print('Digite a data de vencimento do produto:')
data_vencimento[int(input('Ano: '))] = {int(input('Mês: ')): int(input('Dia: '))}

# def verifica_validade(ano_vencimento: int, mes_vencimento: int, dia_vencimento: int):
#     ano_vencimento = data_vencimento[0]
#     mes_vencimento = data_vencimento[0][0]
#     dia_vencimento = data_vencimento[0][1]

    

