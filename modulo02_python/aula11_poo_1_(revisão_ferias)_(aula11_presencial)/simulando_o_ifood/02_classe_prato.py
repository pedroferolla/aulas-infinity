# REVISÃO DE FÉRIAS - POO

# 2 - Criar Classe Prato:
    # Objetivo: crie uma classe 'Prato', com os seguintes atributos:
        
        # nome: nome do prato
        # preco: preço do prato
        # descricao: descrição do prato

    # Adicione o método 'mostrar_prato()', que deve exibir as informações do prato, incluindo nome, preço e descrição.

    # Tarefa: crie três pratos:
        # 1 - Cheeseburger - R$ 22,50 - 'Hambúrguer com queijo cheddar, alface, tomate e molho especial.'
        # 2 - Batata Frita - R$ 12,00 - 'Porção de batatas fritas crocantes.'
        # 3 - Salada de Alface - R$ 8,00 - 'Salada fresca de alface, tomate e cenoura.'

        # Crie objetos para esses pratos e chame o método 'mostrar_prato()' para exibir os dados de cada prato.

    # Output esperado:
        # Nome do prato: Cheeseburger
        # Preço: R$ 22.50
        # Descrição: Hambúrguer com queijo cheddar, alface, tomate e molho especial.

        # Nome do prato: Batata Frita
        # Preço: R$ 12.00
        # Descrição: Porção de batatas fritas crocantes.

        # Nome do prato: Salada de Alface
        # Preço: R$ 8,00
        # Descrição: Salada fresca de alface, tomate e cenoura

class Prato:
    def __init__(self, nome_do_prato: str, preco: float, descricao: str):
        self.nome_do_prato = nome_do_prato
        self.preco = preco
        self.descricao = descricao

    def mostrar_prato(self):
        print('PRATO:')
        print('_'*75)

        print(f'Nome do prato: {self.nome_do_prato}')
        print(f'Preço: {self.preco:.2f}')
        print(f'Descrição: {self.descricao}')


prato_1 = Prato('Cheeseburger', 22.5, 'Hambúrguer com queijo cheddar, alface, tomate e molho especial.')
prato_2 = Prato('Batata Frita', 12, 'Porção de batatas fritas crocantes.')
prato_3 = Prato('Salada de Alface', 8, 'Salada fresca de alface, tomate e cenoura')

prato_1.mostrar_prato()
prato_2.mostrar_prato()
prato_3.mostrar_prato()
