# EXERCÍCIOS DE FIXAÇÃO
# Args

# 1 - Crie uma função chamada 'soma_numeros', que aceite um número variável de argumentos e retorne a soma de todos eles.

    # Input:
    # soma_numeros(5, 10, 15)

    # Resultado esperado:
    # 30

def soma_numeros(*args):
    for numero in args:
        numero += numero
    return numero

print(soma_numeros(5, 10, 15))
