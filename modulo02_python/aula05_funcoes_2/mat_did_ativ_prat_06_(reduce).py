# ATIVIDADE PRÁTICA 6

# Crie uma função que aceita uma lista de strings e use a função reduce (importada de functools) para encontrar a maior 
# string na lista.

from functools import reduce

# lista_strings = ['1', '123', '12']
lista_strings = ['Milito', 'treinador', 'argentino', 'desgraçado']

maior_string = reduce(lambda x, y: x if len(x) > len(y) else y, lista_strings)     # <---- DÚVIDA

print(maior_string)


# RESOLUÇÃO DA DÚVIDA: para comparar tamanho de string é necessário utilizar o len().
