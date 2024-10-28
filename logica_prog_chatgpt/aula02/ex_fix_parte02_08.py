# EXERCÍCIOS DE FIXAÇÃO - PARTE2/2

# 8 - Escreva um programa que verifica o número do dia da semana (1 a 7) digitado pelo usuário e imprime o nome do dia correspondente.

numero = input('Digite um número (1 a 7): ')

if numero == '1':
    print('Domingo')
elif numero == '2':
    print('Segunda-feira')
elif numero == '3':
    print('Terça-feira')
elif numero == '4':
    print('Quarta-feira')
elif numero == '5':
    print('Quinta-feira')
elif numero == '6':
    print('Sexta-feira')
elif numero == '7':
    print('Sábado')
else:
    print('Número inválido')
