# DESAFIOS
# 3 - Jogo da memória com listas
# Dificuldade: ***

# Vocês devem criar um jogo de memória simples.
# Terá uma lista de palavras e o jogador precisa adivinhar onde estão as palavras repetidas.

# Passos:
    # 1 - Crie uma lista de palavras com pares (total de 10 palavras, ou seja, 5 pares).
        # palavras = ['gato', 'gato', 'cachorro', 'cachorro', 'pássaro', 'pássaro', 'cavalo', 'cavalo', 'boi', 'boi']

    # 2 - Embaralhe a lista, para isso é só fazer:
        # import random    <--------- Colocar o import na primeira linha de código
        # random.shuffle(lista)

    # 3 - Peça para o jogador escolher duas posições da lista para revelar as palavras.
    # 4 - Se as palavras forem iguais, remova-as da lista, caso contrário, enconda-as novamente.
    # 5 - O jogo termina quando todos os pares forem encontrados.

import random

palavras = ['gato', 'gato', 'cachorro', 'cachorro', 'pássaro', 'pássaro', 'cavalo', 'cavalo', 'boi', 'boi']
random.shuffle(palavras)

posicao_max = 9

# print(palavras)   <---- Impressão para teste

print('\nJogo da memória:')

while len(palavras) > 1:
    palpite1 = int(input(f'\nEscolha a primeira posição (entre 0 e {posicao_max}): '))
    print(palavras[palpite1])
    palpite2 = int(input(f'Escolha a segunda posição (entre 0 e {posicao_max}): '))
    print(palavras[palpite2])

    if palavras[palpite1] == palavras[palpite2]:
        palavras.pop(palpite1)
        palavras.pop(palpite2 - 1)

        posicao_max -= 2

        print('\nCerta resposta!')

    else:
        print('Você errou!')

    if len(palavras) == 0:
        print('\nParabéns! Você ganhou 1 milhão de Reais em barras de ouro, que valem mais do que dinheiro!')
        break

    # print(palavras)   <---- Impressão para teste
