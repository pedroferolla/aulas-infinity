# DOMÍNIO

# 1 - Criando um Gerenciador de Tarefas com Python
    # Imagine que você está criando um aplicativo simples para organizar suas tarefas diárias.
    # Este aplicativo tem algumas funcionalidades principais:
        # - Adicionar Tarefa: adiciona uma nova tarefa à sua lista.
        # - Listar Tarefas: exibe todas as suas tarefas, mostrando se estão pendentes ou concluídas.
        # - Marcar Tarefa como Conluída: atualiza o status de uma tarefa para 'concluída'.
        # - Remover Tarefa: exclui uma tarefa da lista.

    # Vamos agora transformar essas funcionalidades em um programa Python com um menu interativo, onde você pode escolher 
    # o que deseja fazer.

    # Siga as etapas abaixo para construir esse sistema!

    # Passo 1: Armazenando as Tarefas
        # Comece criando uma lista chamada 'tarefas' para armazenar as informações de cada tarefa.
        # Cada tarefa será representada por um dicionário, com a descrição e o status (se está 'pendente' ou 'concluída').

        # tarefas = []   <---- Lista que armazena as tarefas.

        # Por exemplo:
        # tarefas = [
        #     {'Descrição': 'Estudar Python', 'Status': 'Pendente'},
        #     {'Descrição': 'Fazer supermercado', 'Status': 'Concluído'}
        # ]                                                                                         <--------- OK

    # Passo 2: Função para Adicionar Tarefa
        # Crie uma função chamada 'adicionar_tarefa', que adiciona uma tarefa à lista de tarefas.
        # A função deve receber a descrição da tarefa e adicionar o status como 'Pendente'.

        # def adicionar_tarefa(descricao: str):
        #     Escreva seu código aqui

        # Teste sua função com uma descrição fixa de tarefa:
        # adicionar_tarefa('Estudar Python')                                                        <--------- OK

    # Passo 3: Função para Listas as Tarefas
        # Agora, implemente a função 'listar_tarefas', que irá mostrar todas as tarefas com o seu respectivo 
        # status ('Pendente' ou 'Concluído').
        # Se a lista estiver vazia, a função deverá exibir uma mensagem dizendo 'Nenhuma tarefa disponível.'.

        # Suponha as seguintes tarefas:
        # tarefas = [
        #     {'Descrição': 'Estudar Pyhton', 'Status': 'Pendente'},
        #     {'Descrição': 'Fazer supermercado', 'Status': 'Concluído'}
        # ]

        # O progrma deverá mostrar:
        # [1] Estudar Pyhton - Pendente
        # [2] Fazer supermercado - Concluído

        # DICA: para enumerar as tarefas, observe o código a seguir.
        # lista = ['a', 'b', 'c']
        # for indice, valor in enumerate(lista, start = 1):
        #     print(f'Índice: {indice} - Valor: {valor}')

        # O resultado será:
        # Índice: 1 - Valor: a
        # Índice: 2 - Valor: b
        # Índice: 3 - Valor: c

        # Adapte o código acima para poder enumerar a sua lista de tarefas.                        <----------- OK

    # Passo 4: Função para Marcar uma Tarefa como Concluída
        # Após mostrar as tarefas no passo 3, crie a função 'marcar_concluida', fazendo com que mostre as tarefas e, 
        # após o usuário terminar uma tarefa, ele informa um número e muda o status daquela tarefa, de pendente para 
        # concluída.

        # TAREFAS:
        # [1] Estudar Pyhton - Pendente
        # [2] Fazer supermercado - Concluído
        # Qual tarefa você deseja concluir? 1    <---- Número fornecido pelo usuário
        # Tarefa 1 concluída com sucesso.

        # LISTA ATUALIZADA:
        # [1] Estudar Pyhton - Conluído
        # [2] Fazer supermercado - Concluído

        # Antes de fazer isso, verifique se o índice informado é válido (não pode ser menor que 0 ou maior que o número 
        # total de tarefas).

    # Passo 5: Função para Remover uma Tarefa
        # Impremente a função 'remover_tarefa', que recebe o índice da tarefa e a remove da lista.
        # Também, assim como no caso de marcar como concluída, valide o índice para garantir que ele está dentro do 
        # intervalo correto.

    # Passo 6: Criando o Menu Interativo
        # Agora, vamos criar um menu que permitirá ao usuário escolher qual funcionalidade deseja usar.

        # O menu terá as seguintes opções:
        # [1] Adicionar uma nova tarefa.
        # [2] Listar as tarefas.
        # [3] Marcar uma tarefa como concluída.
        # [4] Remover uma tarefa.
        # [5] Sair do programa.


# 1:
tarefas = []
tarefas = [
    {'Descrição': 'Estudar Pyhton', 'Status': 'Pendente'},
    {'Descrição': 'Fazer supermercado', 'Status': 'Concluído'},
]


# 2:
def adicionar_tarefa(descricao: str):
    nova_tarefa = {}
    nova_tarefa['Descrição'] = descricao
    nova_tarefa['Status'] = 'Pendente'

    tarefas.append(nova_tarefa)

## Maneira mais didática:
def adicionar_tarefa2(descricao_informada: str):
    tarefa_nova = {
        'Descrição': descricao_informada,
        'Status': 'Pendente'
    }

    tarefas.append(tarefa_nova)

# adicionar_tarefa2(descricao_informada = input('\nDigite a tarefa a ser adicionada: '))

# 3:
def listar_tarefas(tarefas: list):
    if len(tarefas) == 0:
        print('\nNenhuma tarefa disponível.')
    else:
        indice = 1
        print('\nTAREFAS:')
        for item in tarefas:
            print(f"[{indice}] {item['Descrição']} - {item['Status']}")
            indice += 1

# listar_tarefas(tarefas)

## Usando 'enumerate':
def tarefas_listar(tarefas: list):
    if len(tarefas) == 0:
        print('\nNenhuma tarefa disponível.')
    else:
        print('\nTAREFAS:')
        for indice, tarefa in enumerate(tarefas, start = 1):
            print(f"[{indice}] {tarefa['Descrição']} - {tarefa['Status']}")

# tarefas_listar(tarefas)


# 4:
def marcar_concluida(indice_tarefa: int):
    if indice_tarefa <= 0 or indice_tarefa > len(tarefas):
        print('Índice inválido.')
    else:
        tarefas[indice_tarefa - 1]['Status'] = 'Concluído'
        print(f'Tarefa {indice_tarefa} concluída com sucesso.')

    print('\nLISTA ATUALIZADA:')
    for indice, tarefa in enumerate(tarefas, start = 1):
        print(f"[{indice}] {tarefa['Descrição']} - {tarefa['Status']}")

# tarefas_listar(tarefas)
# indice_tarefa = int(input('Qual tarefa você deseja concluir? '))

# marcar_concluida(indice_tarefa)


# 5:
def remover_tarefa(indice_tarefa: int):
    if indice_tarefa <= 0 or indice_tarefa > len(tarefas):
        print('Índice inválido.')
    else:
        tarefas.pop(indice_tarefa - 1)
        print(f'Tarefa {indice_tarefa} removida com sucesso.')

    print('\nLISTA ATUALIZADA:')
    for indice, tarefa in enumerate(tarefas, start = 1):
        print(f"[{indice}] {tarefa['Descrição']} - {tarefa['Status']}")

# tarefas_listar(tarefas)
# indice_tarefa = int(input('\nQual tarefa você deseja remover? '))

# remover_tarefa(indice_tarefa)


# 6:
print('\nBem-vindo(a) ao Gerenciador de Tarefas!')

while True:
    print('\nMENU:')
    print('[1] Adicionar uma nova tarefa.')
    print('[2] Listar as tarefas.')
    print('[3] Marcar uma tarefa como concluída.')
    print('[4] Remover uma tarefa.')
    print('[5] Sair do programa.')

    opcao = input('\nDigite o número da opção desejada: ')

    if opcao == '1':
        adicionar_tarefa(descricao = input('\nDigite a tarefa a ser adicionada: '))
    
    elif opcao == '2':
        listar_tarefas(tarefas)
    
    elif opcao == '3':
        tarefas_listar(tarefas)
        indice_tarefa = int(input('\nQual tarefa você deseja concluir? '))
        marcar_concluida(indice_tarefa)

    elif opcao == '4':
        tarefas_listar(tarefas)
        indice_tarefa = int(input('\nQual tarefa você deseja remover? '))
        remover_tarefa(indice_tarefa)

    elif opcao == '5':
        print('\nPrograma encerrado.')
        break

    else:
        print('\nOpção inválida.\nTente novamente.')
