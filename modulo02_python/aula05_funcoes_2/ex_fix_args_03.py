# EXERCÍCIOS DE FIXAÇÃO
# Args

# 3 - Crie uma função chamada 'concatena_strings', que aceite um número variável de argumentos e retorne uma única string, 
    # que é a concatenação de todas as strings fornecidas.

    # Input:
    # concatena_strings('Olá', ' ', 'Mundo', '!')

    # Resultado esperado:
    # 'Olá Mundo!'

def concatena_strings(*args):
    string_concatenada = ''
    for string in args:
        string_concatenada += string
    return string_concatenada

print(concatena_strings('Olá', ' ', 'Mundo', '!'))
