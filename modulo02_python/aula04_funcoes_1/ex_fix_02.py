# EXERCÍCIOS DE FIXAÇÃO

# 2 - Crie uma função chamada 'dividir' que receba dois parâmetros: 'a' e 'b'.
    # A função deve retornar a divisão de 'a' e 'b'.

    # Input:
        # a = 10
        # b = 2

    # Resultado esperado:
        # 5.0

def dividir(a: float, b: float):
    divisao = a / b
    return divisao

# Resolução 1:
a = 10
b = 2
divisao1 = dividir(a, b)
print(f'Divisão 1: {divisao1}')


# Resolução 2:
divisao2 = dividir(10, 2)
print(f'Divisão 1: {divisao1}')
