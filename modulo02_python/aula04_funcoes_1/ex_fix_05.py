# EXERCÍCIOS DE FIXAÇÃO

# 5 - Função 'string_vazia'
    # Crie uma função chamada 'string_vazia' que receba um parâmetro texto.
    # A função deve retornar 'True' se a string estiver vazia e 'False' caso contrário.

    # Input:
        # texto_1 = ''
        # texto_2 = 'aula de programação'

    # Resultado esperado:
        # True   <---- Para texto_1
        # False   <---- Para texto_2

def string_vazia(texto: str):
    resultado = None
    if texto == '':
        resultado = True
    else:
        resultado = False
    
    return resultado

# Resolução 1:
texto_1 = ''
resultado1 = string_vazia(texto_1)
print(resultado1)

texto_2 = 'aula de programação'
resultado2 = string_vazia(texto_2)
print(resultado2)


# Resolução 2:
resultado3 = string_vazia('')
print(resultado3)

resultado4 = string_vazia('aula de programação')
print(resultado4)
