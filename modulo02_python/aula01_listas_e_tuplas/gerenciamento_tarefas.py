# EXERCÍCIOS DE FIXAÇÃO

# Gerenciamento de Tarefas:

# 1 - Crie uma lista chamada tarefas que contenha cinco tarefas diferentes que você precisa realizar.
# 2 - Peça ao usuário para adicionar uma nova trarefa à lista e imprima a lista atualizada.
# 3 - Peça ao usuário para informar o índice de uma tarefa que deseja remover da lista e imprima a lista atualizada.
# 4 - Imprima todas as tarefas conforme o exemplo abaixo:
    # [] lavar louça
    # [] comprar carne
    # [] estudar programação
# 5 - Peça ao usuário para marcar uma tarefa como concluída.
    # Ele irá informar o índice de uma tarefa que foi concluída e a remover da lista de tarefas pendentes.
# 6 - Conte quantas tarefas ainda estão pendentes e mostre na tela.
# 7 - Faça um menu com as opções de adicionar, remover, mostrar tarefas pendentes, marcar como concluída e contar quantas 
    # tarefas estão pendentes.

# 1:
lista_tarefas = [
    'Lavar louça',
    'Comprar carne',
    'Estudar programação',
    'Levar o cachorro pra passear',
    'Abastecer o carro'
]

# 2:
# tarefa_adicionar = input('Insira uma nova tarefa na lista: ')
# lista_tarefas.append(tarefa_adicionar)
# print(lista_tarefas)

# 3:
# tarefa_remover = int(input('Digite o índice de uma tarefa para removê-la da lista: '))
# lista_tarefas.pop(tarefa_remover)
# print(lista_tarefas)

# 4:
indice_tarefa = 0

print('\nLista de tarefas:')
for i in lista_tarefas:
    print(f'{indice_tarefa} - {i}')
    indice_tarefa += 1

# 5:
# tarefa_concluida = int(input('Digite o índice de uma tarefa concluída para removê-la da lista: '))
# lista_tarefas.pop(tarefa_concluida)

# 6:
# print(len(lista_tarefas))

# 7:


while True:
    print('\nMENU:')
    print('[1] Adicionar tarefa.')
    print('[2] Remover tarefa.')
    print('[3] Mostrar tarefas pendentes.')
    print('[4] Marcar como concluída.')
    print('[5] Quantidade de tarefas pendentes.')
    print('[6] Encerrar programa.')

    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        tarefa_adicionar = input('Insira uma nova tarefa na lista: ')    # <------- Obs: Como evitar valores indevidos?
        lista_tarefas.append(tarefa_adicionar)
        print(lista_tarefas)
    elif opcao == '2':
        tarefa_remover = int(input('Digite o índice de uma tarefa para removê-la da lista: '))
        lista_tarefas.pop(tarefa_remover)
        print(lista_tarefas)
    elif opcao == '3':
        print(lista_tarefas)
    elif opcao == '4':
        tarefa_concluida = int(input('Digite o índice de uma tarefa concluída para removê-la da lista: '))
        lista_tarefas.pop(tarefa_concluida)
        print(lista_tarefas)
    elif opcao == '5':
        print(f'\n{len(lista_tarefas)} tarefas pendentes.')
    elif opcao == '6':
        print('\nEncerrando programa.')
        break
    else:
        print('\nOpção inválida. Tente novamente.')
