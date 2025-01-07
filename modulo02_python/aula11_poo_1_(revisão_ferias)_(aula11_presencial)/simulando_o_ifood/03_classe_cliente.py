# REVISÃO DE FÉRIAS - POO

# 3 - Criar Classe Cliente:
    # Objetivo: crie uma classe 'Cliente', com os seguintes atributos:
        # nome: nome do cliente
        # endereco: endereço do cliente
        # telefone: telefone de contato do cliente

    # Adicione o método 'mostrar_dados_cliente()', que deve exibir as informações do cliente, incluindo nome, endereço e telefone.

    # Tarefa: crie um cliente chamado 'Carlos Silva', com os seguintes dados:
        # Endereço: 'Rua A, 123'
        # Telefone: '1234-5678'

    # Crie um objeto dessa classe e chame o método 'mostrar_dados_cliente()' para exibir os dados do cliente.

    # Output esperado:
        # Nome do cliente: Carlos Silva
        # Endereço: Rua A, 123
        # Telefone: 1234-5678

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


cliente_1 = Cliente('Carlos Silva', 'Rua A, 123', '1234-5678')

cliente_1.mostrar_dados_cliente()
