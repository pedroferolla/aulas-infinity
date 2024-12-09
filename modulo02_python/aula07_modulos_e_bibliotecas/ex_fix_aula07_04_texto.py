# EXERCÍCIO DE FIXAÇÃO

# 4 - Manipulação de Strings em um Módulo:
    # Crie um módulo chamado 'texto.py', com as seguintes funções:
        # - Contar palavras em uma frase
        # - Converter o texto em letras maiúsculas
        # - Inverter o texto
        # - Converter o texto em letras minúsculas

    # No arquivo 'principal.py', importe o módulo 'texto' e aplique as funções:
        # - Conte as palavras na frase: 'Olá mundo'
        # - Transforme o texto 'python é divertido' em maiúsculas
        # - Transforme o texto 'PYHTON É DIVERTIDO', gerado anteriormente, em letras minúsculas
        # - Inverta o texto 'ABCDE'

    # Mostre os resultado no console.

def contar_palavras(frase: str):
    contador_espacos = 0
    for caractere in frase:
        if caractere == ' ':
            contador_espacos += 1

    palavras_contadas = contador_espacos + 1

    return palavras_contadas

def converter_em_maisculas(frase: str):
    texto_em_maisculas = frase.upper()

    return texto_em_maisculas

def inverter_texto(frase: str):
    indice_caractere = -1
    texto_invertido = ''

    for caractere in frase:
        texto_invertido += frase[indice_caractere]
        indice_caractere -= 1

    return texto_invertido

def converter_em_minusculas(frase: str):
    texto_em_minusculas = frase.lower()

    return texto_em_minusculas
