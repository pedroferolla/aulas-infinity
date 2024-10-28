# EXERCÍCIOS DE APRENDIZAGEM

# 2 - Crie um programa que leia dois números e mostre um menu na tela:
    # [1] somar
    # [2] multiplicar
    # [3] descobrir qual é o maior
    # [4] mudar os dois números
    # [5] sair do programa

    # Seu programa deverá realizar a operação solicitada em cada caso. Caso a opção seja inválida,
    # deverá mostrar o menu novamente.

# RESULTADO ESPERADO:
    # Digite o primeiro número: 10
    # Digite o segundo número: 5
    # [1] somar
    # [2] multiplicar
    # [3] descobrir qual é o maior
    # [4] mudar os dois números
    # [5] sair do programa
    # Escolha uma opção: 2
    # ----------------------------
    # O produto de 10 e 5 é: 50

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

while True:
    print('\nMenu:')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] DESCOBRIR QUAL É O MAIOR')
    print('[4] MUDAR OS DOIS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')

    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif opcao == '2':
        print(f'{num1} x {num2} = {num1 * num2}')
    elif opcao == '3':
        if num1 > num2:
            print(f'Maior número: {num1}')
        elif num1 < num2:
            print(f'Maior número: {num2}')
        else:
            print('Os números são iguais.')
    elif opcao == '4':
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    elif opcao == '5':
        print('Encerrando o programa.')
        break
    else:
        opcao = input('Opção inválida. Tente novamente: ')
