class Pessoa:
    def __init__(self, nome_informado: str, idade_informada: int):
        self.nome = nome_informado
        self.idade = idade_informada

    def teste_se_e_menor_de_idade(self):
        if self.idade < 18:
            print(f'A pessoa {self.nome} é menor de idade.')
        else:
            print(f'A pessoa {self.nome} é maior de idade.')

    def fazer_aniversario(self):
        self.idade += 1



pessoa1 = Pessoa('Cleiton', 30)
pessoa1.teste_se_e_menor_de_idade()
print(f'Idade antes do aniversário: {pessoa1.idade}')
pessoa1.fazer_aniversario()
print(f'Idade depois do aniversário: {pessoa1.idade}')

pessoa2 = Pessoa('Sara', 14)
pessoa2.teste_se_e_menor_de_idade()

