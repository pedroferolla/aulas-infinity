# EXERCÍCIOS DE FIXAÇÃO - PARTE 1/2

# Dado o dicionário "aluno" com as seguintes chaves e valores:
    # "nome": "João"
    # "nota": 7.5

# Adicione a nova chave "curso" com o valor "Matemática".
# Imprima o dicionário após adicionar a nova chave, mostrando todas as chaves e valores presentes.

aluno = {
    'nome': 'João',
    'nota': 7.5
}

aluno['curso'] = 'Matemática'

print(aluno)

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')
