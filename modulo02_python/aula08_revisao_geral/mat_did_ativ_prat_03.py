# ATIVIDADE PRÁTICA 3

# Crie um conjunto (set) com nomes de cores.
# Implemente uma função que retorne as cores que têm mais de quatro letras.

conjunto = {'laranja', 'branco', 'verde', 'preto', 'rosa', 'azul', 'amarelo'}

novo_conjunto = set()

def retorna_mais_de_quatro_letras(x = set):
    for cor in x:
        if len(cor) > 4:
            novo_conjunto.add(cor)

    return novo_conjunto

print(retorna_mais_de_quatro_letras(x = conjunto))
