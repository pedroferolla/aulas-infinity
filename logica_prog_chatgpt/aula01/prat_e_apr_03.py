# Pratique e aprenda

# Objetivo:
    # Peça ao usuário para digitar seu nome, idade e cidade natal.
    # Use uma f-string para formatar e exibir uma mensagem com essas informações.

# Instruções:
    # 1 - Solicitar o nome do usuário:
        # Use a função input() para pedir ao usuário que insira seu nome.

    # 2 - Solicitar a idade do usuário:
        # Use a função input() para pedir ao usuário que insira sua idade.
        # Converta a entrada do usuário, de string para un número (int).

    # 3 - Solicitar a cidade natal do usuário:
        # Use a função input() para pedir ao usuário que insirua sua cidade natal.

    # 4 - Formatar e exibir a mensagem com f-string:
        # Use uma f-string para formatar a mensagem com as informações fornecidas pelo usuário e exiba a mensagem usando a função print().

# Benefícios: praticar a criação e uso de f-strings e incluir variáveis e expressões.

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade_natal = input('Digite sua cidade natal: ')

print(f'Olá {nome}, você tem {idade} anos e nasceu em {cidade_natal}.')
