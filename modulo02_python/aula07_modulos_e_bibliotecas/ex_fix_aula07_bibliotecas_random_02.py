# EXERCÍCIO DE FIXAÇÃO

# Exercício 2: Sorteio de Prêmios
    # Crie um programa que sorteie aleatoriamente o vencedor de um prêmio em uma lista de participantes.
    # Permita que o usuário insira a lista de participantes e o número de prêmios a serem sorteados.
    # O programa deve garantir que a mesma pessoa não ganhe mais de um prêmio.

# random.sample(lista, k)

from random import sample

numero_de_participantes = int(input('\nDigite o número de participantes: '))

indice_participante = 0
lista_participantes = []

numero_de_premios = int(input('Digite o número de prêmios: '))
lista_sorteados = []

print('\nDigite os nomes dos participantes:')

while indice_participante < numero_de_participantes:
    indice_participante += 1
    adicionar_participante = input(f'{indice_participante}º participante: ')
    lista_participantes.append(adicionar_participante)

lista_sorteados.append(sample(lista_participantes, numero_de_premios))

print('\nSorteados:')

for sorteados in lista_sorteados:
    for sorteado in sorteados:
        print(sorteado)
