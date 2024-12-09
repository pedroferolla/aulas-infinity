# ATIVIDADE PRÁTICA 5

# Desenvolva um programa que permita ao usuário converter entre diferentes unidades de medida, como:
    # - Metros para pés
    # - Quilogramas para libras
    # - Celsius para Fahrenheit.

# Use módulos que contenham funções de conversão.

import mat_did_ativ_prat_aula07_05_conversores as conv

print('\nCONVERSOR DE MEDIDAS')

while True:
    print('\nMenu:')
    print('[1] Metros para pés')
    print('[2] Quilogramas para libras')
    print('[3] Celsius para Fahrenheit')
    print('[4] Sair')

    opcao_usuario = input('Digite uma opção: ')

    if opcao_usuario == '1':
        metros = float(input('\nMetros: '))
        print(f'Comprimento em pés: {conv.converter_metros_para_pes(metros):.2f}')

    elif opcao_usuario == '2':
        quilos = float(input('\nQuilogramas: '))
        print(f'Peso em libras: {conv.converter_quilogramas_para_libras(quilos):.2f}')

    elif opcao_usuario == '3':
        celsius = float(input('\n°Celsius: '))
        print(f'Temperatura em °Fahrenheit: {conv.converter_celsius_para_fahrenheit(celsius):.1f}')

    elif opcao_usuario == '4':
        print('\nPrograma encerrado')
        break

    else:
        print('\nOpção inválida.')
