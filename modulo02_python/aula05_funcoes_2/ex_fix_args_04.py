# EXERCÍCIOS DE FIXAÇÃO
# Args

# 4 - Crie uma função chamada 'media_numeros', que aceite um número variável de argumentos e retorne a média aritmética dos 
    # números fornecidos.

    # Input:
    # media_numeros(4, 8, 12, 16)

    # Resultado esperado:
    # 10

def media_numeros(*args):
    indice = 0
    soma = 0
    for numero in args:
        soma += numero
        indice += 1

    media = soma / indice

    return media

print(media_numeros(4, 8, 12, 16))
