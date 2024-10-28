# ESTRUTURA WHILE TRUE

# É usada para criar loops infinitos, que continuam a executar até que uma condição interna interrompa o loop usando break.
# Útil quando a condição de término é complexa ou baseada em eventos desconhecidos antecipadamente.

# Exemplo: verificação de senha.

while True:
    print('\nMenu:')
    print('1. Diga Olá')
    print('2. Diga Adeus')
    print("Digite 'sair' para terminar o programa.")

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print('Olá!')
    elif opcao == '2':
        print('Adeus!')
    elif opcao.lower() == 'sair':
        print('Encerrando o programa.')
        break
    else:
        print('Opção inválida, tente novamente.')

# Explicação: O menu continua a ser exibido até que o usuário digite "sair".
            # A estrutura while True permite que o menu seja repetido indefinidamente, com break para sair do loop.
