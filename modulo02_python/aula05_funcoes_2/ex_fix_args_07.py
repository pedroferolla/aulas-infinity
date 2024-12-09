# EXERCÍCIOS DE FIXAÇÃO
# Args

# 7 - Crie uma função chamada 'formatar_numeros', que aceite um número variável de argumentos e retorne uma lista com os 
    # números formatados como strings, com duas casas decimais.

    # Input:
    # formatar_numeros(1.123, 2.456, 3.789)

    # Resultado esperado:
    # ['1.12', '2.46', '3.79']

def formatar_numeros(*args):
    lista_numeros_formatados = []

    for numero in args:
        numero_arredondado = round(numero, 2)

        numero_formatado = str(numero_arredondado)

        lista_numeros_formatados.append(numero_formatado)

    return lista_numeros_formatados

print(formatar_numeros(1.123, 2.456, 3.789))
