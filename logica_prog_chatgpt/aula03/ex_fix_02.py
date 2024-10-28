# EXERCÍCIOS DE FIXAÇÃO

# 2 - Faça um programa que peça uma nota, entre zero e dez.
    # Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# RESULTADO ESPERADO:
    # Digite uma nota entre zero e dez: 15
    # Nota inválida. Por favor, digite uma nota entre zero e dez.

    # Digite uma nota entre zero e dez:: -3
    # Nota inválida. Por favor, digite uma nota entre zero e dez.

    # Digite uma nota entre zero e dez: 7.5
    # Você digitou uma nota válida: 7.5

nota = float(input('Digite a nota entre zero e dez: '))

# while nota < 0 or nota > 10:
#     nota = float(input('Nota inválida. Por favor, digite uma nota entre zero e dez: '))

# print(f'Você digitou uma nota válida: {nota}')


# while True:
#     if nota >= 0 and nota <= 10:
#         print(f'Você digitou uma nota válida: {nota}')
#         break
#     else:
#         nota = float(input('Nota inválida. Por favor, digite uma nota entre zero e dez: '))


while True:
    if nota < 0 or nota > 10:
        nota = float(input('Nota inválida. Por favor, digite uma nota entre zero e dez: '))
    else:
        print(f'Você digitou uma nota válida: {nota}')
        break
