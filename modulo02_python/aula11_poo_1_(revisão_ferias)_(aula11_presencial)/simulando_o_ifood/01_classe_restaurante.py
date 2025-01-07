# REVISÃO DE FÉRIAS - POO

# 1 - Criar Classe Restaurante:
    # Objetivo: crie uma classe 'Restaurante', com os atributos 'nome', 'tipo_cozinha' e 'avaliacao_media'.
              # Adicione o método 'mostrar_informacoes()' para exibir os dados do restaurante.

    # Tarefa: crie um restaurante chamado 'Hamburgueria do João', que serve 'Hambúrgueres' e tem uma avaliação de 4.5.
            # Crie um objeto dessa classe e chame o método 'mostrar_informacoes()' para exibir as informações.

    # Deverá mostrar:
        # Nome do Restaurante: Hamburgueria do João
        # Tipo de Cozinha: Hambúrgueres
        # Avaliação Média: 4.5

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


restaurante_1 = Restaurante('Hamburgueria do João', 'Hambúrgueres', 4.5)

restaurante_1.mostrar_informacoes()
