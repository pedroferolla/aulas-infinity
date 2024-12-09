# ATIVIDADE PRÁTICA 2

# Crie um módulo chamado 'manipulacao_strings', que contenha funções para realizar operações com strings, como inverter uma 
# string, contar o número de palavras em uma string e verificar se uma string é um palíndromo (lê-se igual de trás para 
# frente).
# Crie um programa principal que importe o módulo e use essas funções com strings fornecidas pelo usuário.

def inverter_string(string: str):
    indice_caractere = -1
    string_invertida = ''

    for caractere in string:
        string_invertida += string[indice_caractere]
        indice_caractere -= 1

    return string_invertida

def contar_palavras_string(frase: str):
    contador_espacos = 0
    for caractere in frase:
        if caractere == ' ':
            contador_espacos += 1

    palavras_contadas_string = contador_espacos + 1

    return palavras_contadas_string

def string_palindromo(string: str):
    if string == inverter_string(string):
        return f'{string} é um palíndromo!'
    else:
        return f'{string} não é um palíndromo.'
