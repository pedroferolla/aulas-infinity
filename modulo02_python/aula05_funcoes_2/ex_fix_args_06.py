# EXERCÍCIOS DE FIXAÇÃO
# Args

# 6 - Crie uma função chamada 'verificar_presenca', que aceite um número variável de argumentos e um argumento adicional que 
    # deve ser verificado.
    # A função deve retornar True, se o argumento adicional estiver presente na lista de argumentos variáveis, e False, caso 
    # contrário.

    # Input 1:
    # verificar_presenca(5, 1, 2, 3, 4, 5)

    # Resultado esperado 1:
    # True

    # Input 2:
    # verificar_presenca(6, 1, 2, 3, 4, 5)

    # Resultado esperado 2:
    # False

def verificar_presenca(*args, arg_adicional: int):
    if arg_adicional in args:
        argumento_presente = True
    else:
        argumento_presente = False

    return argumento_presente

input_1 = verificar_presenca(5, 1, 2, 3, 4, arg_adicional= 5)
print(input_1)

input_2 = verificar_presenca(6, 1, 2, 3, 4, arg_adicional= 5)
print(input_2)
