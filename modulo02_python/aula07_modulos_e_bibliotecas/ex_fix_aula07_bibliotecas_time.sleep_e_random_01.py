# EXERCÍCIO DE FIXAÇÃO

# 1 - Faça um jogo de par ou ímpar, que sorteie um número de 1 a 10 para o computador.
    # O jogador deverá escolher também um número entre 1 e 10.
    # A cada 1 segundo, mostre um ponto '.' e, ao final de 3 segundos, mostre o que o PC escolheu e qual o resultado 
    # da partida.

from random import(
    randint,
    choice)
from time import sleep

opcoes = ['par', 'ímpar']

print('\nPAR OU ÍMPAR?')

escolha_pc = choice(opcoes)
print(f'Computador escolhe: {escolha_pc}')

numero_pc = randint(1, 10)
numero_jogador = int(input('Escolha um número entre 1 e 10: '))

soma = numero_pc + numero_jogador

if soma % 2 == 0 and escolha_pc == 'par':
    vencedor = 'Computador'
elif soma % 2 != 0 and escolha_pc == 'par':
    vencedor = 'Jogador'
elif soma % 2 == 0 and escolha_pc == 'ímpar':
    vencedor = 'Jogador'
elif soma % 2 != 0 and escolha_pc == 'ímpar':
    vencedor = 'Computador'

sleep(1)
print('.')

sleep(1)
print('.')

sleep(1)
print('.')

sleep(1)

print(f'Escolha do computador: {numero_pc}')
print(f'{numero_pc} + {numero_jogador} = {soma}')
print(f'Vencedor: {vencedor}')
