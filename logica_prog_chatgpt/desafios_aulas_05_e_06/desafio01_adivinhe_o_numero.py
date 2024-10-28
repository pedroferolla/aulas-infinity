# 1 - ADIVINHE O NÚMERO
# Dificuldade: *

# Objetivo: O jogador deve adivinhar um número secreto ferado pelo computador.
          # O programa deve gerar um número aleatório entre 1 e 20.
          # Para isso, colocar o código abaixo:
            # import random
            # numero_secreto = random.randint(1,10)

          # O jogador tem que adivinhar o número, e o programa deve fornecer feedback se o palpaite foi muito alto,
          # muito baixo, ou correto.
          # O jogo continua até que o jogador adivinhe corretamente. VOcê irá precisar de utilizar o While.

import random
numero_secreto = random.randint(1,10)

# numero_secreto = 5   <------- Teste com variável fixa

numero_usuario = int(input('Digite um número: '))

while numero_usuario != numero_secreto:
    if numero_usuario > numero_secreto:
        if numero_usuario > 10:
            print('Número inválido!')
        else:
            print('Número muito baixo.')
    elif numero_usuario < numero_secreto:
        if numero_usuario < 1:
            print('Número inválido!')
        else:
            print('Número muito baixo.')

    numero_usuario = int(input('Tente novamente: '))

print(f'Número correto! O número é: {numero_secreto}')


# CÓDIGO CONTÉM ERRO QUANDO ENTRA NÚMERO NEGATIVO - APURAR
