# EXERCÍCIOS DE FIXAÇÃO

# 3 - Função 'eh_positivo'
    # Crie uma função chamada 'eh_positivo' que receba um parâmetro 'numero'.
    # A função deve retornar 'True' se o número for positivo e 'False' se não for.

    # Input:
        # numero = 5

    # Resultado esperado:
        # True


def eh_positivo(numero: float):
    ele_eh_positivo = None
    if numero > 0:
        ele_eh_positivo = True
    else:
        ele_eh_positivo = False
    return ele_eh_positivo

# Resolução 1:
numero_1 = 2
resultado_1 = eh_positivo(numero_1)
print(resultado_1)


# Resolução 2:
print(eh_positivo(-65))
