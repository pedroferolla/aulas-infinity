# DESAFIOS

# 1 - Caixa eletrônico:
    # Faça um programa para um caixa eletrônico.
    # O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas.

# OBSERVAÇÕES:
    # a. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
    # b. O valor mínimo é de 10 reais e o máximo de 600 reais.
    # c. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# EXEMPLOS:
    # a. Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1.
    # b. Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor_saque = int(input('Valor do saque: R$ '))
notas_100 = 0
notas_50 = 0
notas_10 = 0
notas_5 = 0
notas_1 = 0

if valor_saque >= 10 and valor_saque <= 600:
    notas_100 += valor_saque // 100
    if notas_100 > 0:
        print(f'{notas_100} nota(s) de R$ 100,00')
    notas_50 += (valor_saque - (notas_100 * 100)) // 50
    if notas_50 > 0:
        print(f'{notas_50} nota(s) de R$ 50,00')
    notas_10 += (valor_saque - ((notas_100 * 100) + (notas_50 * 50))) // 10
    if notas_10 > 0:
        print(f'{notas_10} nota(s) de R$ 10,00')
    notas_5 += (valor_saque - ((notas_100 * 100) + (notas_50 * 50) + (notas_10 * 10))) // 5
    if notas_5 > 0:
        print(f'{notas_5} nota(s) de R$ 5,00')
    notas_1 += (valor_saque - ((notas_100 * 100) + (notas_50 * 50) + (notas_10 * 10) + (notas_5 * 5))) // 1
    if notas_1 > 0:
        print(f'{notas_1} nota(s) de R$ 1,00')
else:
    print('Não é possível sacar abaixo de R$ 10,00 ou acima de R$ 600,00.')


# GABARITO:
# Solicita ao usuário o valor do saque:
# saque = int(input('Digite o valor que deseja sacar (entre 10 e 600 reais): '))

# Verifica se o valor do saque está dentro do intervalo permitido:
# if saque < 10 or saque > 60:
    # print('Valor de saque inválido. O valor deve estar entre 10 e 600 reais.')
# else:
    # Inicializa o contador de cada tipo de nota

    # notas_100 = saque // 100
    # saque = saque % 100
    
    # notas_50 = saque // 50
    # saque = saque % 50

    # notas_10 = saque // 10
    # saque = saque % 10

    # notas_5 = saque // 5
    # saque = saque % 5

    # notas_1 = saque

# Imprime o resultado:
# print(f'Para sacar a quantia de {saque} reais, o programa fornece:')
    # if notas_100 > 0:
        # print(f'{notas_100} nota(s) de 100 reais')
    # if notas_50 > 0:
        # print(f'{notas_50} nota(s) de 50 reais')
    # if notas_10 > 0:
        # print(f'{notas_10} nota(s) de 10 reais')
    # if notas_5 > 0:
        # print(f'{notas_5} nota(s) de 5 reais')
    # if notas_1 > 0:
        # print(f'{notas_1} nota(s) de 1 real')
