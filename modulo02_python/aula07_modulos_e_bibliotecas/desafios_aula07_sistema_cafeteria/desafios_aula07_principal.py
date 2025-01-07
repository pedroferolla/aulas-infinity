# DESAFIOS

# SISTEMA DE CAFETERIA
    # Vamos criar um sistema de gerenciamento para um café, que lida com produtos como cafés, chás e bolos.

    # 1 - O sistema terá três módulos distintos:
        # 1 - Arquivo 'produtos.py': gerencia os produtos do café, incluindo o nome do produto, quantidade em estoque e 
            # preço.
        # 2 - Arquivo 'vendas.py': calcula o valor total das vendas e adiciona novas vendas.
        # 3 - Arquivo 'relatorio.py': gera e exibe relatórios de vendas e estoque.

    # O programa 'principal.py' utilizará funções desses três módulos para gerenciar o inventário, registrar vendas e gerar 
    # relatórios.

    # Estrutura de arquivos:
        # meu_projeto/
            # |--- principal.py
            # |--- produtos.py
            # |--- vendas.py
            # |--- relatório.py


    # Passos para realizar o exercício:

    # 2.1 - Arquivo 'produtos.py':
        # Gerenciar produtos disponíveis no café.

        # Funções a serem implementadas:
            # adicionar_produto(): recebe o nome, a quantidade de estoque, preço de um produto e o inventário (uma lista de
                                 # dicionários), que tem todos os produtos.

                                 # inventário = [
                                      # {'nome_produto': {
                                            # 'quantidade_disponível': total_quantidade,
                                            # 'preco': valor_preco,
                                            # 'vendas': [lista_de_vendas]
                                            # }
                                      # }
                                 # ]

                # Exemplo:
                    # inventario = [
                    #      {'café': {
                    #           'quantidade_disponível': 78,
                    #           'preco': 2.99,
                    #           'vendas': [5.98, 2.99, 11.96]
                    #           }
                    #      }
                    # ]

            # adicionar_estoque(): atualiza a quantidade do estoque de um produto. Recebe o nome do produto, a quantidade 
                                 # de estoque que chegou e o inventário de produtos.

                    # Produto Capuccino foi adicionado com sucesso!

                # Deverá retornar a mensagem de erro abaixo, caso o produto não tenha sido encontrado:
                    # Produto {nome} não encontrado no inventário.

            # listar_produtos(): recebe o inventário e o nome de todos os produtos do café.

                # Exemplo:
                    # Lista de produtos:
                    # Café
                    # Chá verde
                    # Bolo de chocolate

            # listar_produtos_e_precos(): recebe o inventário e lista o nome de todos os produtos com seus respectivos 
                                        # preços do café.

                # Exemplo:
                    # Café - R$ 5.00
                    # Chá verde - R$ 3.50
                    # Bolo de chocolate - R$ 7.00

            # listar_informacoes_produtos(): recebe o inventário e lista o nome de todos os produtos com seus respectivos 
                                           # preços e quantidades do café.

                # Exemplo:
                    # Café:
                    # quantidade_disponivel: 20
                    # preco: 5.0
                    # vendas: []

                    # Chá verde:
                    # quantidade_disponivel: 15
                    # preco: 3.50
                    # vendas: []

                    # Bolo de chocolate:
                    # quantidade_disponivel: 10
                    # preco: 7.0
                    # vendas: []


    # 2.2 - Arquivo 'vendas.py':
        # Calcular o valor total das vendas e registrar novas vendas.

        # Funções a serem implementadas:
            # registrar_venda(): recebe o nome, quantidade vendida e o inventário de produtos. Deverá subtrair a quantidade 
                               # vendida do produto apenas se houver quantidade suficiente.

                               # Caso não tenha a quantidade suficiente, deverá mostrar a mensagem:
                                    # Produto {nome} não tem quantidade suficiente. No estoque há apenas {quantidade no 
                                    # estoque}.

                               # Caso seja registrada a venda de um produto que não existe no inventário, exibir:
                                    # Produto {nome} não está cadastrado no nosso sistema.

            # calcular_total_vendas(): recebe o inventário e mostra o total vendido de cada produto.
                # {'Café': 25.0, 'Chá verde': 21.0, 'Bolo de chocolate': 77.0, 'Capuccino': 0}


    # 2.3 - Arquivo 'relatorio.py':
        # Gerar e exibir relatórios sobre o estoque e as vendas.

            # gerar_relatorio_estoque(): recebe o inventário e mostra a quantidade de cada produto do café.
                # Relatório de estoque:
                # Café: 15 unidades
                # Chá verde: 9 unidades
                # Bolo de chocolate: 1 unidade

            # gerar_relatorio_vendas(): recebe o inventário e o valor total de vendas de cada produto.
                # Relatório de vendas:
                # Café: R$ 25.00
                # Chá verde: R$ 21.00
                # Bolo de chocolate: R$ 63.00

            # exibir_relatorios(): recebe o inventário para mostrar os relatórios de estoque e vendas juntos.
                # Relatório de estoque:
                # Café: 15 unidades
                # Chá verde: 9 unidades
                # Bolo de chocolate: 1 unidade

                # Relatório de vendas:
                # Café: R$ 25.00
                # Chá verde: R$ 21.00
                # Bolo de chocolate: R$ 63.00


    # 2.4 - Arquivo 'principal.py':
        # Objetivo: integrar as funções dos módulos para gerenciar o inventário, registrar vendas e gerar relatórios.

        # Cadastre os seguintes produtos:
            # Produto             Qnt   Preço
            # Café Expresso       20    R$ 5,00
            # Chá Verde           15    R$ 3,50
            # Bolo de Chocolate   10    R$ 7,00

    # TESTANDO O PROGRAMA
    # Venda:
        # 3 cafés expressos
        # 9 bolos de chocolate
        # 2 cafés expressos
        # 6 chás verdes

    # Ao chamar o relatório, deverá retornar algo como:
        # ------------------------------
        # Relatório de Estoque:
        # ------------------------------
        # Café: 15 unidades
        # Chá Verde: 9 unidades
        # Bolo de Chocolate: 1 unidades
        # ------------------------------
        # Relatório de Vendas:
        # ------------------------------
        # Café: R$ 25.00
        # Chá Verde: R$ 21.00
        # Bolo de Chocolate: R$ 63.00

    # Tente vender mais 2 bolos de chocolate e deverá retornar um erro:
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # Produto Bolo de Chocolate não tem quantidade suficiente. No estoque há apenas 1.
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # Adicione 1 bolo de chocolate ao estoque e venda 2 bolos de chocolate. Deverá retornar algo como:
        # ------------------------------
        # Relatório de Estoque:
        # ------------------------------
        # Café: 15 unidades
        # Chá Verde: 9 unidades
        # Bolo de Chocolate: 0 unidades
        # ------------------------------
        # Relatório de Vendas:
        # ------------------------------
        # Café: R$ 25.00
        # Chá Verde: R$ 21.00
        # Bolo de Chocolate: R$ 77.00

    # Liste os produtos do café:
        # -------------------
        # Lista de produtos:
        # -------------------
        # Café
        # Chá Verde
        # Bolo de Chocolate

    # Adicione o produto cappuccino, com 12 unidades e um preço de R$ 6.00:
        # {'Café': 5.0, 'Chá Verde': 3.5, 'Bolo de Chocolate': 7.0, 'Cappuccino': 6.0}

    # Gere um relatório que mostre todos os detalhes de todos os produtos:
        # Café
        # **************************
        # quantidade_disponivel: 15
        # preco: 5.0
        # vendas: [15.0, 10.]

        # **************************
        # Chá Verde
        # **************************
        # quantidade_disponivel: 9
        # preco: 3.5
        # vendas: [21.0]

        # **************************
        # Bolo de Chocolate
        # **************************
        # quantidade_disponivel: 0
        # preco: 7.0
        # vendas: [64.0, 14.0]

        # **************************
        # Cappuccino
        # **************************
        # quantidade_disponivel: 12
        # preco: 6.0
        # vendas: []

        # **************************

    # Mostre o total de vendas de cada produto:
    # O resultado deverá ser:
        # {'Café': 25.00, 'Chá Verde': 21.0, 'Bolo de Chocolate': 77.0, 'Cappuccino': 0}
