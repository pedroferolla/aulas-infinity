# 4 - RESOLVA A CONTA
# Dificuldade: ****

# Objetivo: O jogador deve resolver problemas matemáticos gerados pelo programa.

# Descrição:
    # O programa gera duas operações matemáticas aleatórias (soma, subtração, multiplicação ou divisão) e
    # pede ao jogador que resolva.

    # Para sortear a operação, utilize o código abaixo:
        # Gera números e operador aleatórios:
        # operador = random.choice(['+', '-', '*', '/'])
        # num1 = random.randit(1, 10)
        # num2 = random.randit(1, 10)

        # Ajusta o divisor para garantir que a divisão seja exata:
        # if operador == '/':
            # num2 = random.randint(1, 10)
            # num1 = num2 * random.randint(1, 10)

    # O jogador deve inserir a resposta e o programa verifica se está correta ou não.
    # O jogo pode continuar com um número definido de perguntas ou até que o jogador queira parar.

import random

operador = random.choice(['+', '-', '*', '/'])
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

if operador == '/':
    num2 = random.randint(1, 10)
    num1 = num2 * random.randint(1, 10)

resultado = num1 + operador + num2
resposta_usuario = int(input(f'{num1} {operador} {num2} = '))

if resposta_usuario == resultado:
    print('Certa resposta!')
else:
    print('Você errou!')

# DÚVIDA: COMO CONVERTER O OPERADOR DE STRING PARA OPERADOR NUMÉRICO?
