# FORCA

# Crie um programa que implemente o jogo da forca. O jogo deve funcionar da seguinte maneira:

    # Escolha de palavra: o programa deve escolher aleatoriamente uma palavra de uma lista de palavras.

    # Tentativas: o usuário deve ter um número limitado de tentativas (por exemplo, 6) para adivinhar as letras da palavra.

    # Exibição da palavra: a palavra deve ser exibida com as letras adivinhadas corretamente e as letras não adivinhadas 
    # devem ser mostradas como underscores (_). Por exemplo, se a palavra for "pyhton" e o usuário adivinhou "p" e "t", 
    # a exibição deve ser "p_t_ _ _".

    # Feedback: o programa deve informar ao usuário se a letra adivinhada está correta ou não.

    # Finalização: O jogo termina quando o usuário adivinha a palavra completa ou esgota suas tentativas.
    # O programa deve informar se o usuário venceu ou perdeu.

import random
lista = ['cachorro', 'gato', 'papagaio']
palavra = ''

palavra = random.randint[lista]
print(palavra)

# DÚVIDA: COMO RANDOMIZAR STRINGS?
