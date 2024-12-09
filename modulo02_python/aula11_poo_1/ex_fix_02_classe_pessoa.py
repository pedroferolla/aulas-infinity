# EXERCÍCIOS DE FIXAÇÃO

# 2 - Classe 'Pessoa':
    # Contexto: você quer registrar informações sobre pessoas em uma escola de idiomas.

    # Tarefa:
        # 1 - Crie uma classe chamada 'Pessoa', com os atributos 'nome', 'idade' e 'idioma'.
        # 2 - Crie um método chamado 'apresentar', que exibe uma frase como:
            # Exemplo: 'Oi, meu nome é Ana, tenho 25 anos e estou aprendendo Inglês.'

        # 3 - Instancie três objetos da classe 'Pessoa', com os seguintes dados:
            # Pessoa 1: nome = 'Ana', idade = 25, idioma = 'Inglês'
            # Pessoa 2: nome = 'Carlos', idade = 30, idioma = 'Espanhol'

        # 4 - Use o método 'apresentar' para exibir as apresentações.

class Pessoa:
    def __init__(self, nome: str, idade: int, idioma: str):
        self.nome = nome
        self.idade = idade
        self.idioma = idioma

    def apresentar(self):
        print(f'Oi, meu nome é {self.nome}, tenho {self.idade} e estou aprendendo {self.idioma}.')



pessoa_1 = Pessoa('Ana', 25, 'Inglês')
pessoa_2 = Pessoa('Carlos', 30, 'Espanhol')
pessoa_3 = Pessoa('Ector Tusclêncio', 37, 'Russo')

pessoa_1.apresentar()
pessoa_2.apresentar()
pessoa_3.apresentar()
