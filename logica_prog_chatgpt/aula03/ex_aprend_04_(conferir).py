# EXERCÍCIOS DE APRENDIZAGEM

# 4 - Escreva um programa que imprima o seguinte padrão:

# RESULTADO ESPERADO:
    # *
    # **
    # ***
    # ****
    # *****

asteryx = '*'
linha = input('Digite Enter para saltar uma linha (X para encerrar): ')

while True:
    print(asteryx)
    asteryx += '*'
    linha = input('Digite Enter para saltar uma linha: ')

    if linha == 'X':
        print('Tchau querida!')
        break


# CONFERIR SE O ENUNCIADO FOI COMPREENDIDO, PORQUE NA PRIMEIRA TENTATIVA GEROU-SE UM LOOP INFINITO.
