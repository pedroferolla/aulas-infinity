# 2 - PEDRA, PAPEL OU TESOURA
# Dificuldade: **

# Objetivo: Jogar contra o computador e aplicar lógica para determinar o vencedor.

# Descrição:
    # O computador faz uma escolha aleatória e o jogador escolhe entre "pedra", "papel" ou "tesoura".
    # Para sortear a escolha do computador, rodar o código abaixo:
        # import random

        # Lista com as opções:
        # opcoes = ["pedra", "papel", "tesoura"]

        # Sorteia uma opção:
        # escolha = random.choice(opcoes)

    # O programa determina o vencedor de acordo com as regras: pedra ganha de tesoura, tesoura ganha de papel,
    # papel ganha de pedra.
    # Perguntar se o jogador quer jogar novamente.

import random
opcoes = ['pedra', 'papel', 'tesoura']

while True:
    escolha = random.choice(opcoes)
    jogador = input('\nPedra, papel ou tesoura? (Escolha uma opção): ')

    while jogador != 'pedra' and jogador != 'papel' and jogador != 'tesoura':
        jogador = input('\nDigite uma opção válida: ')

    if jogador == 'pedra' and escolha == 'tesoura':
        print(f'\nEscolha do jogador: {jogador}')
        print(f'Escolha do computador: {escolha}')
        print('Parabéns! Você ganhou do computador!')
    elif jogador == 'tesoura' and escolha == 'pedra':
        print(f'\nEscolha do jogador: {jogador}')
        print(f'Escolha do computador: {escolha}')
        print('Você perdeu!')

    elif jogador == 'tesoura' and escolha == 'papel':
        print(f'\nEscolha do jogador: {jogador}')
        print(f'Escolha do computador: {escolha}')
        print('Parabéns! Você ganhou do computador!')
    elif jogador == 'papel' and escolha == 'tesoura':
        print(f'\nEscolha do jogador: {jogador}')
        print(f'Escolha do computador: {escolha}')
        print('Você perdeu!')

    elif jogador == 'papel' and escolha == 'pedra':
        print(f'\nEscolha do jogador: {jogador}')
        print(f'Escolha do computador: {escolha}')
        print('Parabéns! Você ganhou do computador!')
    elif jogador == 'pedra' and escolha == 'papel':
        print(f'\nEscolha do jogador: {jogador}')
        print(f'Escolha do computador: {escolha}')
        print('Você perdeu!')

    elif jogador == escolha:
        print(f'\nEscolha do jogador: {jogador}')
        print(f'Escolha do computador: {escolha}')
        print('Empate!')


    jogar_novamente = input('\nJogar novamente? (Sim ou Não): ')
    while jogar_novamente != 'Sim' and jogar_novamente != 'Não':
        jogar_novamente = input('Digite uma opção válida (Sim ou Não): ')

    if jogar_novamente == 'Não':
        print('Jogo encerrado.')
        break
            
# Obs: ciente de que o código pode e deve melhorar, para ficar mais objetivo.
     # Será revisto adiante, mas, por hora, entrega o que foi solicitado pelo enunciado.
