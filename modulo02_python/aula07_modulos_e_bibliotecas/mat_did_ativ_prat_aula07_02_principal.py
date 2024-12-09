# ATIVIDADE PRÁTICA 2

# Crie um módulo chamado 'manipulacao_strings', que contenha funções para realizar operações com strings, como inverter uma 
# string, contar o número de palavras em uma string e verificar se uma string é um palíndromo (lê-se igual de trás para 
# frente).
# Crie um programa principal que importe o módulo e use essas funções com strings fornecidas pelo usuário.

from mat_did_ativ_prat_aula07_02_manipulacao_strings import *

print('\nMANIPULADOR DE PALAVRAS')

while True:
    print('\nMenu:')
    print('[1] Inverter uma palavra.')
    print('[2] Contar o número de palavras em uma frase.')
    print('[3] Verificar se a palavra é um palíndromo.')
    print('[4] Encerrar programa.')

    escolha_usuario = input('\nDigite o índice para a operação desejada: ')

    if escolha_usuario == '1':
        string = input('\nDigite a palavra a ser invertida: ')
        print(f'\n{string} invertida: {inverter_string(string)}')

    elif escolha_usuario == '2':
        frase = input('\nDigite a frase para contagem de palavras: ')
        print(f'Número de palavras na frase: {contar_palavras_string(frase)}')

    elif escolha_usuario == '3':
        string = input('\nDigite uma palavra para verificar se é um palíndromo: ')
        print(string_palindromo(string))

    elif escolha_usuario == '4':
        print('Programa encerrado.')
        break

    else:
        print('Opção inválida.')
