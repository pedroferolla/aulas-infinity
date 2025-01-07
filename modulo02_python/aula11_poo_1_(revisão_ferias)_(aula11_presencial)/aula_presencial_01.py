class Produto:
    def __init__(self, nome: str, preco: float, cor: str, qnt_estoque: int):
        self.nome = nome
        self.preco = preco
        self.cor = cor
        self.qnt_estoque = qnt_estoque

class CarrinhoDeCompras:
    def __init__(self):
        self.lista_produtos = []

    def adicionar_produtos(self, produto: Produto):
        self.lista_produtos.append(produto)

    def visualizar_produtos(self):
        print('_'*50)
        print('Lista de produtos do carrinho:')
        print('_'*50)
        if self.lista_produtos != []:
            for produto in self.lista_produtos:
                print(produto.nome)

    def calcular_preco_total(self):
        soma = 0
        for produto in self.lista_produtos:
            soma += produto.preco
        print(f'O total é: R$ {soma}')

    

produto_1 = Produto('Relógio', 15000, 'Prata', 1)

# Após terminar a classe Produto, crie 3 produtos.
# Depois, criar uma classe de carrinho de compras

produto_2 = Produto('Computador', 5000, 'Branco', 5)
produto_3 = Produto('Renault Kwid', 285000, 'Burro fugido', 2)
produto_4 = Produto('TV', 7000, 'Preto', 10)

carrinho_1 = CarrinhoDeCompras()
print(f'Antes: {carrinho_1.lista_produtos}')

carrinho_1.adicionar_produtos(produto_2)
carrinho_1.adicionar_produtos(produto_2)
carrinho_1.adicionar_produtos(produto_3)

carrinho_1.visualizar_produtos()
carrinho_1.calcular_preco_total()

