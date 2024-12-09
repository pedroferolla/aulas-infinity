# Prova PYIA - Módulos e Bibliotecas

# Crie uma função chamada 'lancar_dados', que utilizará o módulo random para simular o lançamento de dois dados.
# Cada dado deve gerar um número aleatório entre 1 e 6.
# A função deve somar os resultados desses dois lançamentos e retornar o valor total.

import random

def lancar_dados():
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    soma = dado_1 + dado_2

    return print(f'Dado 1: {dado_1}\nDado 2: {dado_2}\nSoma: {soma}')

lancar_dados()
