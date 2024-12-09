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

from ex_fix_aula07_04_texto import *

print(contar_palavras('Olá mundo'))

palavra_em_maiscula = converter_em_maisculas('python é divertido')
print(palavra_em_maiscula)

print(converter_em_minusculas(palavra_em_maiscula))

print(inverter_texto('ABCDE'))
