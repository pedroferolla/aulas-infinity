# DESAFIOS
# 1 - Adivinhação de números com tuplas
# Dificuldade: *

# Vocês devem criar um jogo de adivinhação onde o jogador precisa adivinhar um número escolhido aleatoriamente de uma 
# tupla de números.

# O jogo dá dicas se o número é maior ou menor que o palpite.

# Requisitos:
    # 1 - O seu programa deverá sortear um número entre 1 a 10, de forma aleatória.
    # 2 - O jogador faz um palpite e o jogo dá dicas se o número é maior ou menor.
    # 3 - O jogo continua até o jogador acertar o número.

# Passos:
    # 1 - Crie uma tupla com números de 1 a 10 com:
        # numeros = tuple(range(1, 11))

    # 2 - Escolha aleatoriamente um número da tupla, com:
        # import random   <--- colocar o import na primeira linha de código
        # numero_secreto = random.choice(numeros)

    # 3 - O jogador faz um palpite e o jogo dá dicas se o número é maior ou menor.

    # 4 - O jogo continua até o jogador 

import random

numeros = tuple(range(1, 11))
numero_secreto = random.choice(numeros)

print('\nBem-vindo ao jogo de adivinhação!')
palpite = int()

while palpite != numero_secreto:
    palpite = int(input('Escolha um número de 1 a 10: '))

    if palpite < numero_secreto:
        print('O número é maior que o seu palpite.')
    elif palpite > numero_secreto:
        print('O número é menor que o seu palpite')
    else:
        print('Parabéns! Você acertou o número!')
        break
