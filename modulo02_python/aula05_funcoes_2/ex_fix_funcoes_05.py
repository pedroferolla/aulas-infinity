# FUNÇÕES

# 5 - Pedra, papel ou tesoura:
    # Recrie o jogo de pedra, papel ou tesoura, mas utilizando funções:

    # Funções necessárias:
        # escolha_computador():
            # Deve gerar aleatoriamente uma escolha para o computador e retornar a escolha do computador 
            # (pedra, papel ou tesoura).

        # determinar_vencedor():
            # Deve comparar as escolhas do jogador e do computador, e determinar o vencedor.

            # Entrada: escolhas do jogador e do computador.
            # Saída: resultado do jogo (quem ganhou ou se foi um empate).

        # exibir_resultado():
            # Mostrar ao jogador a escolha do computador, a escolha dele e quem ganhou.
           
            # Entrada: escolhas do jogador e do computador, e o resultado do jogo.
            # Saída: mensagem de resultado exibida ao jogador.

import random
lista = ['pedra', 'papel', 'tesoura']

def escolha_computador():
    return random.choice(lista)

escolha_jogador = input('\nEscolha entre pedra, papel ou tesoura: ')
escolha_pc = escolha_computador()

def determinar_vencedor():
    if escolha_pc == 'pedra' and escolha_jogador == 'pedra':
        return '\nEmpate!'
    elif escolha_pc == 'pedra' and escolha_jogador == 'papel':
        return '\nJogador venceu!'
    elif escolha_pc == 'pedra' and escolha_jogador == 'tesoura':
        return '\nComputador venceu!'
    
    elif escolha_pc == 'papel' and escolha_jogador == 'papel':
        return '\nEmpate!'
    elif escolha_pc == 'papel' and escolha_jogador == 'tesoura':
        return '\nJogador venceu!'
    elif escolha_pc == 'papel' and escolha_jogador == 'pedra':
        return '\nComputador venceu!'
    
    elif escolha_pc == 'tesoura' and escolha_jogador == 'tesoura':
        return '\nEmpate!'
    elif escolha_pc == 'tesoura' and escolha_jogador == 'pedra':
        return '\nJogador venceu!'
    elif escolha_pc == 'tesoura' and escolha_jogador == 'papel':
        return '\nComputador venceu!'
    
    else:
        return '\nOpção inválida!'

def exibir_resultado():
    print(f'Escolha do computador: {escolha_pc}')
    print(f'Escolha do jogador: {escolha_jogador}')
    print(determinar_vencedor())

exibir_resultado()


# GABARITO:
# import random

# def escolha_computador():
    # return random.choice(['pedra', 'papel', 'tesoura'])

# def determinar_vencedor(jogador, computador):
    # if jogador == computador:
        # return 'Empate'
    # elif (jogador == 'pedra' and computador == 'tesoura') or \
    #      (jogador == 'papel' and computador == 'pedra') or \
    #      (jogador == 'tesoura' and computador == 'papel'):
        # return 'Jogador'
    # else:
        # return 'Computador'

# def exibir_resultado(jogador, computador, resultado):
    # print(f'Escolha do jogador: {jogador}')
    # print(f'Escolha do computador: {computador}')
    # print(f'Resultado: {resultado} ganhou!')

# def jogo_pedra_papel_tesoura():
    # print('Jogo Pedra, Papel ou Tesoura')
    # jogador = input('Digite sua escolha (pedra, papel ou tesoura): ').lower()

    # if jogador not in ['pedra', 'papel', 'tesoura']:
        # print('Escolha inválida!')
        # return

    # computador = escolha_computador()
    # resultado = determinar_vencedor(jogador, computador)
    # exibir_resultado(jogador, computador, resultado)


# Exemplo de uso:
# jogo_pedra_papel_tesoura()
