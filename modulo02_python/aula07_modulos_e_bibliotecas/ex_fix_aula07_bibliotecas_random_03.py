# EXERCÍCIO DE FIXAÇÃO

# Exercício 3: Jogo da Adivinhação Inversa
    # Neste jogo, o computador pensa em um número entre 1 e 100, e o jogador precisa adivinhar qual é o número.
    # No entanto, o jogador só pode dar um número limite, e o computador dirá se o número pensado está acima ou abaixo desse 
    # limite.
    # A cada tentativa, o jogador pode reduzir o intervalo em que o número pode estar.
    # O objetivo é adivinhar o número com o menor número de tentativas possíveis.

from random import randint

numero_pc = randint(1, 100)
palpite_jogador = int()
tentativas = 0

print('\nJOGO DA AVINHAÇÃO INVERSA')

while palpite_jogador != numero_pc:
    palpite_jogador = int(input('Palpite: '))
    tentativas += 1

    if palpite_jogador < 1 or palpite_jogador > 100:
        print('\nPalpite inválido.')

    elif palpite_jogador < numero_pc:
        print('\nO número é maior que o palpite.')

    elif palpite_jogador > numero_pc:
        print('\nO número é menor que o palpite.')

    else:
        print('\nCerta resposta!')
        print(f'Número de tentativas: {tentativas}')

notas = {'aluno': [10, 8, 9]}