
class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade: int):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f'Depois da venda de {quantidade}, o estoque é de {self.estoque} unidades.')

        else:
            print(f'Estoque insuficiente. Não foi possível vender {quantidade}')

    def repor(self, quantidade: int):
        self.estoque += quantidade

    def exibir_estoque(self):
        print(f'Produto: {self.nome} | Estoque: {self.estoque}')
        


produto_1 = Produto('Notebook', 3500, 10)
print(f'Antes da venda: {produto_1.estoque}')

produto_1.vender(3)
print(f'Depois da venda de 3: {produto_1.estoque}')

produto_1.vender(8)
produto_1.repor(5)
print(f'Depois de repor 5: {produto_1.estoque}')
produto_1.vender(8)
print(f'Depois da venda de 8: {produto_1.estoque}')
