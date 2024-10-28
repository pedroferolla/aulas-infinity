# DESAFIOS

# 1 - Crie um jogo em que o computador escolha um número aleatório entre 1 e 100.
    # O jogador tenta adivinhar o número. O computador informa se é maior ou menor que o escolhido.
    # O jogo termina quando o jogador acerta o número.

    # Para gerar o número aleatório, utilize as duas linhas de código a seguir:
        # import random
        # numero_secreto = random.randint(1,100)

# RESULTADO ESPERADO:
    # O computador escolhe um número aleatório entre 1 e 100. Tente adivinhar qual é!

    # Digite um número: 50
    # O número é menor que 50.

    # Digite um número: 25
    # O número é maior que 25.

    # Digite um número: 37
    # O número é maior que 37.

    # Digite um número: 42
    # Parabéns! Você acertou o número 42.

import random
numero_secreto = random.randint(1,100)

num_usuario = int(input('Digite um número: '))

while num_usuario != numero_secreto:
    if num_usuario < 1 or num_usuario > 100:
        num_usuario = int(input('Número inválido. Digite um número entre 1 e 100: '))

    if num_usuario < numero_secreto:
        print(f'O número é maior que {num_usuario}.')
    elif num_usuario > numero_secreto:
        print(f'O número é menor que {num_usuario}')
    
    num_usuario = int(input('Tente novamente: '))

print(f'Parabéns! Você acertou o número {numero_secreto}')
