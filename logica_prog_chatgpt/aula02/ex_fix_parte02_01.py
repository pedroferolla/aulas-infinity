# EXERCÍCIOS DE FIXAÇÃO - PARTE2/2

# 1 - Escreva um programa que verifica se uma determinada palavra está presente em uma frase.
    # Se estiver, imprima a frase.

frase = input('Digite uma frase: ')
palavra = input('Digite uma palavra para verificar se está presente na frase: ')

if palavra in frase:
    print(frase)
