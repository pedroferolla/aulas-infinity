# EXERCÍCIOS DE FIXAÇÃO

# 1 - Classe 'Carro':
    # Contexto: você está gerenciando uma frota de táxis na sua cidade.

    # Tarefa:
        # 1 - Crie uma classe chamada 'Carro', com os atributos 'marca', 'modelo' e 'ano'.
        # 2 - Crie um método chamado 'exibir_dados', que exiba uma frase com as informações do carro.
        # 3 - Instancie dois objetos da classe 'Carro', com os seguintes dados:
            # - Carro 1: marca = 'Toyota', modelo = 'Corolla', ano = 2020
            # - Carro 2: marca = 'Honda', modelo = 'Civic', ano = 2019

        # 4 - Use o método 'exibir_dados' para mostras as informações de cada carro.

class Carro:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        print(f'Veículo:\nMarca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}')

carro_1 = Carro('Toyota', 'Corolla', 2020)

carro_2 = Carro('Honda', 'Civic', 2019)


carro_1.exibir_dados()
carro_2.exibir_dados()
