# EXERCÍCIOS DE FIXAÇÃO
# Args

# 2 - Crie uma função chamada 'maior_menor', que aceite um número variável de argumentos e retorne uma tupla com o maior e o 
    # menor número entre eles.

    # Input:
    # maior_menor(7, 2, 8, 3)

    # Resultado esperado:
    # (8, 2)

def maior_menor(*args):
    tupla = (max(args), min(args))

    return tupla

print(maior_menor(7, 2, 8, 3))
