# EXERCÍCIOS DE FIXAÇÃO
# Args

# 9 - Crie uma função chamada 'contar_ocorrencias', que aceite um número variável de argumentos e conte o número de vezes que 
    # cada argumento aparece.

    # Input:
    # contar_ocorrencias('apple', 'banana', 'apple', 'apple', 'banana')

    # Resultado esperado:
    # {'apple': 3, 'banana': 2}

def contar_ocorrencias(*args):
    ocorrencias_contadas = {}
    ocorrencias_apple = 0
    ocorrencias_banana = 0
    
    for arg in args:
        if arg == 'apple':
            ocorrencias_apple += 1
        elif arg == 'banana':
            ocorrencias_banana += 1

    ocorrencias_contadas['apple'] = ocorrencias_apple
    ocorrencias_contadas['banana'] = ocorrencias_banana

    return ocorrencias_contadas

print(contar_ocorrencias('apple', 'banana', 'apple', 'apple', 'banana'))
