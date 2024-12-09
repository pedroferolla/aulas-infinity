# ATIVIDADE PRÁTICA 1

# Crie um programa que será uma calculadora.
# Nesta calculadora, você deverá ter um módulo para as operações matemáticas.
# O arquivo principal deverá conter apenas um menu de escolha para o usuário (soma, subtração, multiplicação e divisão).

from mat_did_ativ_prat_aula07_01_operacoes import *

print('\nCALCULADORA')
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

print('\nEscolha a operação:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
operacao_desejada = input('\nDigite o número da operação desejada: ')

if operacao_desejada == '1':
    print(f'\nResultado: {somar(x, y)}')

elif operacao_desejada == '2':
    print(f'\nResultado: {subtrair(x, y)}')

elif operacao_desejada == '3':
    print(f'\nResultado: {multiplicar(x, y)}')

elif operacao_desejada == '4':
    print(f'\nResultado: {dividir(x, y)}')

else:
    print('Opção inválida.')
