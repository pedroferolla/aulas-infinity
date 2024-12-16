class Aluno:
    def __init__(self, nome: str):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota: float):
        self.notas.append(nota)

aluno1 = Aluno('Prata')
print(aluno1.notas)

aluno1.adicionar_nota(0)
aluno1.adicionar_nota(10)

print(aluno1.notas)
