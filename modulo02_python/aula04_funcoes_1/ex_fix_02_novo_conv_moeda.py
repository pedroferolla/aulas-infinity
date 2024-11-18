# EXERCÍCIOS DE FIXAÇÃO

# 2 - Conversor de Moeda
    # Crie uma função chamada 'converter_real_para_dolar', que recebe um valor em reais e a taxa de conversão atual.
    # A função deve retornar o valor em dólares.

    # Exemplo:
    # converter_real_para_dolar(100, 5.2) deve retornar 19.23

def converter_real_para_dolar(qnt_real: float, taxa: float):
    qnt_dolar = qnt_real / taxa
    return qnt_dolar

print(converter_real_para_dolar(100, 5.77))
