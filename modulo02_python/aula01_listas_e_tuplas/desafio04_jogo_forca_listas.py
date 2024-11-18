# DESAFIOS
# 4 - Jogo da forca com listas
# Dificuldade: ****

# Vocês devem criar um jogo da forca onde o jogador tenta adivinhar uma palavra escolhida aleatoriamente de uma lista.

# Passos:
    # 1 - Crie uma lista de palavras.
        # palavras = ['python', 'gentil', 'programação', 'computador', 'algoritmo', 'nobre', 'afeto']

    # 2 - Escolha uma palavra aleatoriamente.
        # import random   <---- colocar o impor na primeira linha de código
        # palavra_secreta = random.choice(palavras)

    # 3 - O jogador faz palpites de letras.
    # 4 - O jogo informa se a letra está na palavra ou não.
    # 5 - O jogo continua até o jogador adivinhar a palavra ou esgotar o número de tentativas.

import random

palavras = ['python', 'gentil', 'programação', 'computador', 'algoritmo', 'nobre', 'afeto']

palavra_secreta = random.choice(palavras)
# print(palavra_secreta)   # <---- Impressão de teste

tentativas = 10

# palavra_secreta = 'nobre'   # <---- Variável de controle
palavra_secreta_lista = list(palavra_secreta)
palavra_oculta_lista = list(palavra_secreta)

# print(palavra_oculta_lista)   <---- Impressão de teste

indice_letra = 0

for letra in palavra_oculta_lista:
    palavra_oculta_lista[indice_letra] = '_'
    indice_letra += 1

print('\nJogo da forca:')
print(palavra_oculta_lista)


while tentativas > 0:

    palpite_usuario = input('\nDigite uma letra ou palavra para adivinhar a palavra secreta: ')
    tentativas -= 1

    if palpite_usuario == palavra_secreta:
        print('\nParabéns! Você ganhou 1 milhão de Reais em barras de ouro, que valem mais do que dinheiro!')
        print(f'A palavra secreta é: {palavra_secreta}')
        break

    elif palpite_usuario in palavra_secreta:
        indice_palpite = palavra_secreta.index(palpite_usuario)
        palavra_oculta_lista.insert(indice_palpite, palpite_usuario)
        palavra_oculta_lista.pop(indice_palpite + 1)
        tentativas += 1

        print('\nCerta resposta!')
        print(palavra_oculta_lista)
        print(f'{tentativas} tentativas restantes.')

    else:
        print('\nVocê errou!')
        print(palavra_oculta_lista)
        print(f'{tentativas} tentativas restantes.')

    if tentativas == 0:
        print('\nGAME OVER')
