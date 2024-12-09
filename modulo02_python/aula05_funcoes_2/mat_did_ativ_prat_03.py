# ATIVIDADE PRÁTICA 3

# Crie uma função chamada 'concatenar_strings', que aceita um número variável de strings como argumentos 
# posicionais (usando *args).
# A função deve concatenar todas as strings em uma única string e retorná-la.

def concatenar_strings(*args):
    string_concatenada = ''
    for arg in args:
        string_concatenada += arg
    return string_concatenada

print(concatenar_strings('Maria', 'eu', 'sei', 'que', 'você', 'treme', '!'))
