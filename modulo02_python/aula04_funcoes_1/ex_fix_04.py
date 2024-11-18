# EXERCÍCIOS DE FIXAÇÃO

# 4 - Função 'quadrado'
    # Crie uma função chamada 'quadrado' que receba um parâmetro 'numero'.
    # A função deve retornar o quadrado de 'numero'.

    # Input:
        # numero = 4

    # Resultado esperado:
        # 16

def quadrado(numero: float):
    resultado = numero * numero
    return resultado

# Resolução 1:
numero = 4
resultado1 = quadrado(numero)
print(f'O quadrado de {numero} é: {resultado1}')


# Resolução 2:
resultado2 = quadrado(4)
print(f'O quadrado de {numero} é: {resultado2}')
