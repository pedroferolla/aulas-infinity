# APRENDIZAGEM

# 1 - Conversor de Moeda:
    # Crie uma função chamada 'converter_real_para_dolar' que recebe um valor em reais e a taxa de conversão atual.
    # A função deve retornar o valor em dólares.

    # Exemplo: converter_real_para_dolar(100, 5.2) deve retornar 19.23

def converter_real_para_dolar(qnt_reais: float, taxa_dolar: float):
    qnt_dolar = qnt_reais / taxa_dolar
    return qnt_dolar


valor_reais = 100
taxa = 5.2
print(converter_real_para_dolar(valor_reais, taxa))


# Resolução 2:
valor_dolares = converter_real_para_dolar(100, 5.2)
print(f'{valor_dolares:.2f}')
