# DESAFIOS PRÁTICOS

# Instruções:
    # 5 - Adivinhar número:
        # Desenvolva um jogo de adivinhação onde o programa escolhe um número aleatório entre 1 e 100.
        # O usuário deve tentar adivinhar o número, e o programa deve fornecer dicas se o palpite está muito alto ou
        # baixo.

# Benefícios: praticar o uso de operadores aritméticos em Python e entender como realizar cálculos matemáticos
            # básicos com variáveis.


# OBSERVAÇÃO: EXERCÍCIO IDÊNTICO AO APRESENTADO NA AULA 06
            # COMO CRIAR ALEATORIEDADE PELO PROGRAMA SE NÃO FOI VISTA FUNÇÃO RANDOM ATÉ ESTE PONTO DO MATERIAL?

import random
numero_secreto = random.randint(1,100)

# numero_secreto = 5   <------- Teste com variável fixa

numero_usuario = int(input('Digite um número: '))

while numero_usuario != numero_secreto:
    if numero_usuario > numero_secreto:
        if numero_usuario > 100:
            print('Número inválido!')
        else:
            print('Número muito alto.')
    elif numero_usuario < numero_secreto:
        if numero_usuario < 1:
            print('Número inválido!')
        else:
            print('Número muito baixo.')

    numero_usuario = int(input('Tente novamente: '))

print(f'Número correto! O número é: {numero_secreto}')
