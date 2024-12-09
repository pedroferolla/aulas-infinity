# FUNÇÕES

# 1 - Calculadora:
    # Crie um programa de calculadora simples que possa realizar operações básicas (adição, subtração, multiplicação e 
    # divisão) usando funções separadas para cada operação.

    # Peça ao usuário dois números, em seguida, faça um menu de opções para o usuário poder escolher qual função ele quer 
    # executar.

        # 1 - Adição
        # 2 - Subtração
        # 3 - Multiplicação
        # 4 - Divisão

    # Exemplo:
    # Digite o primeiro número: 8
    # Digite o segundo número: 4

    # Escolha a operação:
    # 1 - Adição
    # 2 - Subtração
    # 3 - Multiplicação
    # 4 - Divisão

    # Digite o número da operação desejada: 4

    # Output esperado:
    # Resultado: 2.0

def adicao(x: int, y: int):
    resultado = x + y
    return resultado

def subtracao(x: int, y: int):
    resultado = x - y
    return resultado

def multiplicacao(x: int, y: int):
    resultado = x * y
    return resultado

def divisao(x: int, y: int):
    if y == 0:
        return 'Não é possível dividir por 0'
    resultado = x / y
    return resultado

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

print('\nEscolha a operação:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
operacao_desejada = input('\nDigite o número da operação desejada: ')

if operacao_desejada == '1':
    print(f'\nResultado: {adicao(x, y)}')

elif operacao_desejada == '2':
    print(f'\nResultado: {subtracao(x, y)}')

elif operacao_desejada == '3':
    print(f'\nResultado: {multiplicacao(x, y)}')

elif operacao_desejada == '4':
    print(f'\nResultado: {divisao(x, y)}')
