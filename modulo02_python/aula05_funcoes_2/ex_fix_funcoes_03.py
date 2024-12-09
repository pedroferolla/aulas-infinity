# FUNÇÕES

# 3 - Ordenar lista:
    # Crie um programa que ordene uma lista de números em ordem crescente e decrescente, usando funções separadas para cada 
    # tipo de ordenação.

    # Exemplo:
    # Escolha a ordenação:
    # 1 - Crescente
    # 2 - Decrescente

    # Digite o número da opção desejada: 1

    # Output esperado:
    # Lista em ordem crescente: [1, 2, 3, 5, 8]

    # Passo 1:
    # Crie funções para ordenar uma lista em ordem crescente e decrescente ('ordenar_crescente' e 'ordenar_decrescente').

    # Passo 2:
    # Crie uma função principal ('ordenar_lista'), que permita ao usuário inserir uma lista e escolher o tipo de ordenação.

# lista_usuario = [8, 7, 3, 9, 5]

def ordenar_crescente(lista_usuario: list):
    lista_crescente = []
    while len(lista_usuario) > 0:
        lista_crescente.append(min(lista_usuario))
        lista_usuario.remove(min(lista_usuario))

    return lista_crescente

def ordenar_decrescente(lista_usuario: list):
    lista_decrescente = []
    while len(lista_usuario) > 0:
        lista_decrescente.append(max(lista_usuario))
        lista_usuario.remove(max(lista_usuario))

    return lista_decrescente

def ordenar_lista():
    lista_usuario = []
    print('\nORDENADOR DE LISTAS')

    while len(lista_usuario) < 5:
        novo_numero = int(input('Insira um número para adicionar à lista: '))
        lista_usuario.append(novo_numero)
    print(lista_usuario)

    while True:
        print('\nEscolha a ordenação:\n1 - Crescente\n2 - Decrescente')
        opcao = input('Digite o número da opção desejada: ')

        if opcao == '1':
            print(f'\nLista em ordem crescente: {ordenar_crescente(lista_usuario)}')
            break
        elif opcao == '2':
            print(f'\nLista em ordem decrescente: {ordenar_decrescente(lista_usuario)}')
            break
        else:
            print('\nOpção inválida.')

ordenar_lista()
