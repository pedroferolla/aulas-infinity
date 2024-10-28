# ANINHAMENTO DE WHILE

# O aninhamento de loops while envolve colocar um loop while dentro de outro. É útil para problemas com múltiplas
# camadas de repetição, como iterar sobre matrizes, processar dados complexos ou implementar algoritmos com
# repetição aninhada.

# Exemplo:
    # Este exemplo simula um jogo de adivinhação onde o jogador tem várias tentativas para adivinhar um número secreto.

numero_secreto = 7
tentativas_totais = 3
jogador1_tentativas = 0
jogador2_tentativas = 0

while jogador1_tentativas < tentativas_totais and jogador2_tentativas < tentativas_totais:
    palpite1 = int(input('Jogador 1, adivinhe o número: '))
    jogador1_tentativas += 1
    if palpite1 == numero_secreto:
        print('Jogador 1 acertou!')
        break
    else:
        print('Jogador 1 errou.')

    palpite2 = int(input('Jogador 2, adivinhe o número: '))
    jogador2_tentativas += 1
    if palpite2 == numero_secreto:
        print('Jogador 2 acertou!')
        break
    else:
        print('Jogador 2 errou.')

else:
    print('Ninguém acertou o número secreto.')
