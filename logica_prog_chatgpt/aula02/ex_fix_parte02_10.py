# EXERCÍCIOS DE FIXAÇÃO - PARTE2/2

# 10 - Escreva um programa que verifica o número do mês digitado pelo usuário e imprime a estação do ano correspondente:
    # a. Outono: de março a maio
    # b. Inverno: de junho a agosto
    # c. Primavera: de setembro a novembro
    # d. Verão: de dezembro a fevereiro

mes = input('Digite o número do mês (1 a 12): ')

if mes in ['3', '4', '5']:
    print('Outono')
elif mes in ['6', '7', '8']:
    print('Inverno')
elif mes in ['9', '10', '11']:
    print('Primavera')
elif mes in ['12', '1', '2']:
    print('Verão')
else:
    print('Digite um número de mês válido!')
