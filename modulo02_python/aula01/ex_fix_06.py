# EXERCÍCIOS DE FIXAÇÃO

# 6 - Dada a lista lista = [10, 20, 30, 40, 50], escreva a expressão para verificar se o número 30 está na lista.

    # a. Se o 30 estiver na lista, mostre: "O 30 está na lista."
    # b. Se o 30 não estiver na lista, mostre: "O 30 NÂO está na lista."

lista = [10, 20, 30, 40, 50]

# if 30 in lista:
#     print('O 30 está na lista.')
# else:
#     print('O 30 NÂO está na lista.')


# num = 30

# if num in lista:
#     print(f'O {num} está na lista.')
# else:
#     print(f'O {num} NÂO está na lista.')


num = int(input('Digite um número para saber se ele está na lista: '))

if num in lista:
    print(f'O {num} está na lista.')
else:
    print(f'O {num} NÂO está na lista.')
