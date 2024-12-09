# EXERCÍCIOS DE FIXAÇÃO
# Funções Lambda

# 5 - Crie uma função lambda para verificar se um número dado é negativo.
    # Retorne True se for negativo ou False se não for negativo.

num_e_negativo = lambda x: x < 0

print(num_e_negativo(5))


# Função com def:
def num_negativo(x):
    resultado = x < 5
    return resultado

print(num_negativo(-9))
