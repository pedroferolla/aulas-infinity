# https://dontpad.com/wp-logica-descomplicada

# Código do sistema:

def inicializar_estoque():
    """ Esta função inicializa o estoque.
        Temos um dicionário com outros dicionários.
        Os outros dicionários são os itens do estoque.
        Esses itens também possuem quantidades.

    Returns:
        Estoque, pratos, itens e quantidades.
    """
    return {
        "sanduiche": {
            "pao": 10,
            "mucarela": 10,
            "requeijao": 10,
            "alface": 10,
            "presunto": 10,
            "frango": 10
        },
        "salada": {
            "alface": 10,
            "tomate": 10,
            "cenoura": 10,
            "azeitona": 10
        }
    }


def verificar_estoque(estoque, prato, item, quantidade):
    """ Esta função verifica a disponibilidade do prato e do ingrediente do prato no estoque.

    Returns:
        Caso o prato e item estejam disponíveis, é retornada a quantidade do item solicitado.\n
        Caso o item não esteja no estoque, retorna "False".
    """
    if prato in estoque and item in estoque[prato]:
        return estoque[prato][item] >= quantidade
    return False


def atualizar_estoque(estoque, prato, item, quantidade):
    """ Esta função serve para atualizar o estoque sempre que um prato for produzido.\n
        Primeiro ela verifica a disponibilidade de ingredientes no estoque, através da função 'verificar_estoque()'.

    Returns:
        Se os itens estejam disponíveis, os mesmos são subtraídos do estoque.\n
        Caso contrário, retorna 'False'.
    """
    if verificar_estoque(estoque, prato, item, quantidade):
        estoque[prato][item] -= quantidade
        return True
    return False


def mostrar_estoque(estoque):
    """ Esta função exibe o estoque atual.

    Returns:
        Imprime cada prato e seus respectivos ingredientes, linha por linha.
    """
    print("\nEstoque atual:")
    for prato, itens in estoque.items():
        print(f"\n{prato.capitalize()}:")
        for item, quantidade in itens.items():
            print(f"  {item.capitalize()}: {quantidade}")


def adicionar_ingrediente(estoque, prato, pedido, ingrediente):
    """ Esta função adiciona ingredientes ao prato, após a verificação da disponibilidade do mesmo em estoque.

    Returns:
        Se o ingrediente estiver disponível, o mesmo é removido do estoque e, em seguida, adicionado ao prato.\n
        Caso contrário, é exibida a mensagem comunicando a falta do item no estoque.
    """
    if verificar_estoque(estoque, prato, ingrediente, 1):
        pedido.append(ingrediente)
        atualizar_estoque(estoque, prato, ingrediente, 1)
        print(f"{ingrediente.capitalize()} adicionado ao {prato}!")
    else:
        print(f"Desculpe, {ingrediente} está fora de estoque!")


def mostrar_pedido(prato, pedido):
    """ Esta função exibe o pedido.

    Returns:
        Imprime cada ingrediente do prato, linha a linha, uma vez que a disponibilidade dos ingredientes já foi verificada.\n
        Caso nenhum ingrediente tenha sido adicionado ao pedido, é exibida a mensagem correspondente.
    
    """
    print(f"\nSeu {prato} contém:")
    if pedido:
        for ingrediente in pedido:
            print(f"- {ingrediente.capitalize()}")
    else:
        print(f"Nenhum ingrediente foi adicionado ao {prato} ainda.")


def gerenciar_pedidos():
    """ Esta função inicia o funcionamento do programa.

    Returns:
        Exibe o estoque disponível e imprime a saudação.\n
        Mostra o estoque e os pratos disponíveis.\n
        Solicita o prato desejado e oferece a opção para sair do programa.\n
        Se o prato escolhido estiver disponível no estoque, inicia a montagem do prato e oferece a opção para finalizar.\n
        É oferecida a opção para montar outro pedido e caso contrário, o programa é finalizado, exibindo mensagem de agradecimento.
    """
    estoque = inicializar_estoque()
    print("\nBem-vindo à lanchonete!")

    while True:
        mostrar_estoque(estoque)
        print("\nPratos disponíveis:")
        for prato in estoque.keys():
            print(f"- {prato.capitalize()}")

        prato_escolhido = input("Escolha um prato ou digite 'sair' para encerrar: ").strip().lower()

        if prato_escolhido == 'sair':
            break

        if prato_escolhido in estoque:
            pedido = []
            print(f"\nMonte seu {prato_escolhido}! Selecione um ingrediente por vez.")

            while True:
                print(f"\nMenu de ingredientes para {prato_escolhido}:")
                for item in estoque[prato_escolhido].keys():
                    print(f"- {item.capitalize()}")
                print("- Finalizar")

                escolha = input("Digite o ingrediente ou 'finalizar' para encerrar: ").strip().lower()

                if escolha == "finalizar":
                    break

                if escolha in estoque[prato_escolhido]:
                    adicionar_ingrediente(estoque, prato_escolhido, pedido, escolha)
                else:
                    print("Opção inválida. Tente novamente.")

            mostrar_pedido(prato_escolhido, pedido)
        else:
            print("Prato inválido. Tente novamente.")

        continuar = input("Deseja fazer outro pedido? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\nObrigado por usar nosso sistema! Até logo!")

if __name__ == "__main__":
    gerenciar_pedidos()




# Criando algoritmo:

# 1- Criar um estoque. - Base de dados modelada
# 2- Inicializar o sistema. - Gerenciamento do estoque
# 3 - Laço de repetição - Mostrar ao usuário a lista de pratos disponíveis
# 4 - Solicitar ao usuário que informe o prato desejado
# Verificar a disponibilidade do prato ou encerrar o sistema.
# 5 - Solicitar ao usuário que informe os ingredientes desejados.
# Verificar a disponibilidade de ingredientes.
# 6 - Criar uma lista para receber os pedidos do usuário.
# 7 - Solicitar ao usuário para finalizar o  prato
# 8 - Perguntar ao usuário se deseja fazer um novo pedido ou encerrar o sistema.


# Link para avaliação da aula compartilhada:
# https://forms.gle/WENd9QjbSYWCcDR2A


# https://mapamental.app/
