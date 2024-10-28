opcao = ''

while opcao != 'Sair':
    print('Menu:')
    print('Digite 1 para A.')
    print('Digite 2 para B.')
    print("Digite 'Sair' para encerrar.")
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        print('Você escolheu a opção A.')
    elif opcao == '2':
        print('Você escolheu a opção B.')
    elif opcao == 'Sair':
        print('Encerrando programa.')
    else:
        print('Opção inválida, tente novamente.')

# ERRO: FALTA AO EXEMPLO INSERIR CONDICIONAL PARA EXIBIÇÃO APENAS DA MENSAGEM REFERENTE AO VALOR INSERIDO PELO USUÁRIO E NÃO O MENU.