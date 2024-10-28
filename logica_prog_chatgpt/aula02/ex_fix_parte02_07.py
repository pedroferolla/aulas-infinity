# EXERCÍCIOS DE FIXAÇÃO - PARTE2/2

# 7 - Escreva um programa que verifica se um número é divisível por 5.
    # Se for divisível, imprima "O número é divisível por 5.".

numero = int(input('Digite um número: '))

if numero % 5 == 0:
    print('O número é divisível por 5.')
else:
    print('O número não é divisível por 5.')
