class Restaurante:
    def __init__(self, nome: str, tipo_cozinha: str, avaliacao_media: float):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha
        self.avaliacao_media = avaliacao_media

    def mostrar_informacoes(self):
        print('INFORMAÇÕES:')
        print('_'*50)

        print(f'Nome do Restaurante: {self.nome}')
        print(f'Tipo de Cozinha: {self.tipo_cozinha}')
        print(f'Avaliação Média: {self.avaliacao_media}')


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


class Cliente:
    def __init__(self, nome: str, endereco: str, telefone: str):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def mostrar_dados_cliente(self):
        print('DADOS DO CLIENTE:')
        print('_'*30)

        print(f'Nome do cliente: {self.nome}')
        print(f'Endereço: {self.endereco}')
        print(f'Telefone: {self.telefone}')


class Pedido:
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.pratos = []
        self.status = 'Aguardando finalizar pedido.'

    def adicionar_prato(self, prato: Prato):
        self.pratos.append(prato)

    def mostrar_pedido(self):
        if self.pratos != []:
            print(f'Pedido para: {self.cliente.nome}')
            print('\nPrato(s):')

            for prato in self.pratos:
                print(f'- {prato.nome_do_prato} - R$ {prato.preco:.2f}')

        print(f'\nStatus: {self.status}')

    def alterar_status(self, novo_status: str):
        self.status = novo_status


#####################################################################################
class Entrega:
    def __init__(self, pedido: Pedido, endereço_entrega: str, tempo_estimado: int):
        self.pedido = pedido
        self.endereço_entrega = endereço_entrega
        self.tempo_estimado = tempo_estimado

    def informar_entrega(self, cliente: Cliente):
        print(f'Pedido para: {cliente.nome}')
        print(f'Endereço de entrega: {cliente.endereco}')
        print(f'Tempo estimado: {self.tempo_estimado} minutos')
######################################################################################



restaurante_1 = Restaurante('Hamburgueria do João', 'Hambúrgueres', 4.5)

prato_1 = Prato('Cheeseburger', 22.5, 'Hambúrguer com queijo cheddar, alface, tomate e molho especial.')
prato_2 = Prato('Batata Frita', 12, 'Porção de batatas fritas crocantes.')
prato_3 = Prato('Salada de Alface', 8, 'Salada fresca de alface, tomate e cenoura')

cliente_1 = Cliente('Carlos Silva', 'Rua A, 123', '1234-5678')

pedido_1 = Pedido(cliente_1)
pedido_1.adicionar_prato(prato_1)
pedido_1.adicionar_prato(prato_2)
pedido_1.adicionar_prato(prato_3)

pedido_1.alterar_status('Em preparação.')

pedido_1.mostrar_pedido()

# pedido_1 = Entrega(cliente_1.nome, cliente_1.endereco, tempo_estimado = 30)
# pedido_1.informar_entrega()
