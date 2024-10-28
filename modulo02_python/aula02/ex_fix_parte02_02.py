# EXERCÍCIOS DE FIXAÇÃO - PARTE 2/2

# 2 - A partir do dicionário abaixo, adicione o curso de Biologia para a Ana e remova o curso de Química da Maria.
    # Exiba o dicionário atualizado.

estudantes = {
    "Ana": ["Matemática", "História"],
    "Pedro": ["Biologia", "Física"],
    "Maria": ["Química", "Matemática"]
}

# ADICIONAR UM VALOR À LISTA DENTRO DA CHAVE:
estudantes["Ana"].append('Biologia')

# REMOVER UM VALOR DA LISTA DENTRO DA CHAVE:
estudantes['Maria'].remove('Química')

print(estudantes)
