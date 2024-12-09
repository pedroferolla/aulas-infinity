class Carro:
    def __init__(self, modelo: str, ano: int, cor: str):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def fazer_barulho(self):
        print(f'O carro {self.modelo} está fazendo vrum vrum')

# Criando o objeto carro_1:
carro_1 = Carro('Celta', 2014, 'Prata')

# Criando o objeto carro_2:
carro_2 = Carro('Ônix', 2020, 'Azul pérola')


class Cachorro:
    def __init__(self, nome: str, idade: int, raca: str):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def latir(self):
        print(f'O cachorro {self.nome} latiu: Au au au.')

cachorro_1 = Cachorro('Scooby-Doo', 3, 'Dog Alemão')
cachorro_1.latir()
print(cachorro_1.nome)
