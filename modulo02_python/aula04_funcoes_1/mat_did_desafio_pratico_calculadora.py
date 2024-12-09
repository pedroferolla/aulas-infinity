# DESAFIO PRÁTICO

# Calculadora:
    # Crie uma calculadora com opções de soma, multiplicação, subtração, divisão e sair.
    # (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora)
    # Utilize funções de rotina para cada operação e funções de unidade lógica para realizar os cálculos.
    
    # Dica: utilize de condicionais e laços de repetição para realizar esse exercício.

def somar(num1: float, num2:float):
    soma = num1 + num2

    return soma

def subtrair(num1: float, num2: float):
    subtracao = num1 - num2

    return subtracao

def multiplicar(num1: float, num2: float):
    multiplicacao = num1 * num2

    return multiplicacao

def dividir(num1: float, num2: float):
    divisao = num1 / num2

    return divisao

print('CALCULADORA')

while True:
    print('\nMENU:')
    print('[1] Somar')
    print('[2] Subtrair')
    print('[3] Multiplicar')
    print('[4] Dividir')
    print('[5] Sair do programa.')

    opcao = input('\nDigite o número da opção desejada: ')

    if opcao == '1':
        print(f"Resultado: {somar(num1 = int(input('1º número: ')), num2 = int(input('2º número: ')))}")        
    elif opcao == '2':
        print(f"Resultado: {subtrair(num1 = int(input('1º número: ')), num2 = int(input('2º número: ')))}")
    elif opcao == '3':
        print(f"Resultado: {multiplicar(num1 = int(input('1º número: ')), num2 = int(input('2º número: ')))}")
    elif opcao == '4':
        print(f"Resultado: {dividir(num1 = int(input('1º número: ')), num2 = int(input('2º número: ')))}")
    elif opcao == '5':
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida.\nTente novamente.')
