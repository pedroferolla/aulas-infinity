# ATIVIDADE PRÁTICA 4

# Desenvolva um jogo de adivinhação em que o programa escolhe um número aleatório e desafia o jogador a adivinhá-lo.
# Forneça dicas ao jogador, indicando se o número é maior ou menor do que a adivinhação atual.

import random

print('\nADIVINHE O NÚMERO')

numero_secreto = random.randint(1, 100)

while True:
    palpite_jogador = int(input('\nDigite seu palpite (de 1 a 100): '))

    if palpite_jogador < 1 or palpite_jogador > 100:
        print('Palpite inválido!\nInsira um número entre 1 e 100.')

    elif palpite_jogador > numero_secreto:
        print('Número secreto é menor que o palpite.')

    elif palpite_jogador < numero_secreto:
        print('Número secreto é maior que o palpite.')

    elif palpite_jogador == numero_secreto:
        print('Certa resposta!')
        break

