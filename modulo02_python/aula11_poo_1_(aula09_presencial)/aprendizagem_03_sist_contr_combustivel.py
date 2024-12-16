
class Carro:
    def __init__(self, modelo: str, consumo_por_litro: float):
        self.modelo = modelo
        self.consumo_por_litro = consumo_por_litro
        self.litros_no_tanque = 0

    def abastecer(self, litros: float):
        self.litros_no_tanque += litros

    def dirigir(self, km_quero_andar: float):
        km_percorrivel = self.litros_no_tanque * self.consumo_por_litro
        if km_quero_andar <= km_percorrivel:
            print('Consigo andar!')
            litros_consumidos = km_quero_andar / self.consumo_por_litro
            self.litros_no_tanque -= litros_consumidos

    def exibir_combustivel(self):
        print(f'Modelo: {self.modelo} | Combustível restante: {self.litros_no_tanque} litros.')



carro_1 = Carro('Toro', 6)
carro_1.abastecer(30)
carro_1.dirigir(150)
carro_1.exibir_combustivel()
