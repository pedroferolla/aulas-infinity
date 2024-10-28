# 5 - COMPUTADOR ADIVINHA O NÚMERO
# Dificuldade: *****

# Objetivo: O computador tenta adivinhar o número que o jogador está pensando.

# Descrição:
    # O jogador pensa em um número entre 1 e 100, e o computador tenta adivinhar.
    # O jogador deve fornecer feedback indicando se o palpite do computador é "maior", "menor" ou "correto".
    # O computador ajusta seus palpites com base no feedback, utilizando laços de repetição e condicionais.

import random
# numero_pc = random.randint(1, 100)
# feedback = ''
palpite_certo = 'Certa resposta!'
# numero_correto = int(input('Digite um número inteiro (entre 1 e 100) para o computador tentar adivinhar: '))
numero_correto = 51     # <--------- Variável de controle
piso = 1
teto = 100

numero_pc = random.randint(1, 100)
print(f'Computador: {numero_pc}')
feedback = input('O palpite do computador é (maior, menor ou correto): ')

while True:


    # if feedback == 'correto':
    #     print(palpite_certo)
    #     break

    while feedback == 'maior':
        teto = numero_pc
        numero_pc = random.randint(piso, teto)
        print(f'Computador: {numero_pc}')
        feedback = input('O palpite do computador é (maior, menor ou correto): ')

        # if feedback == 'correto':
        #     print(palpite_certo)
        #     break


        # while feedback == 'maior':
        #     teto = numero_pc
        #     numero_pc = random.randint(piso, teto)
        #     print(f'Computador: {numero_pc}')
        #     feedback = input('O palpite do computador é (maior, menor ou correto): ')

        #     if feedback == 'correto':
        #         print(palpite_certo)
        #         break

        #     elif feedback == 'maior':
        #         teto = numero_pc
        #         numero_pc = random.randint(piso, teto)
        #         print(f'Computador: {numero_pc}')
        #         feedback = input('O palpite do computador é (maior, menor ou correto): ')

        #     elif feedback == 'menor':
        #         piso = numero_pc
        #         numero_pc = random.randint(piso, teto)
        #         print(f'Computador: {numero_pc}')
        #         feedback = input('O palpite do computador é (maior, menor ou correto): ')

        # while feedback == 'menor':
        #     piso = numero_pc
        #     numero_pc = random.randint(piso, teto)
        #     print(f'Computador: {numero_pc}')
        #     feedback = input('O palpite do computador é (maior, menor ou correto): ')

        #     if feedback == 'correto':
        #         print(palpite_certo)
        #         break

        #     elif feedback == 'maior':
        #         teto = numero_pc
        #         numero_pc = random.randint(piso, teto)
        #         print(f'Computador: {numero_pc}')
        #         feedback = input('O palpite do computador é (maior, menor ou correto): ')

        #     elif feedback == 'menor':
        #         piso = numero_pc
        #         numero_pc = random.randint(piso, teto)
        #         print(f'Computador: {numero_pc}')
        #         feedback = input('O palpite do computador é (maior, menor ou correto): ')    


    
    while feedback == 'menor':
        piso = numero_pc
        numero_pc = random.randint(piso, teto)
        print(f'Computador: {numero_pc}')
        feedback = input('O palpite do computador é (maior, menor ou correto): ')

        # if feedback == 'correto':
        #     print(palpite_certo)
        #     break


        # while feedback == 'maior':
        #     teto = numero_pc
        #     numero_pc = random.randint(piso, teto)
        #     print(f'Computador: {numero_pc}')
        #     feedback = input('O palpite do computador é (maior, menor ou correto): ')

        #     if feedback == 'correto':
        #         print(palpite_certo)
        #         break

        #     elif feedback == 'maior':
        #         teto = numero_pc
        #         numero_pc = random.randint(piso, teto)
        #         print(f'Computador: {numero_pc}')
        #         feedback = input('O palpite do computador é (maior, menor ou correto): ')

        #     elif feedback == 'menor':
        #         piso = numero_pc
        #         numero_pc = random.randint(piso, teto)
        #         print(f'Computador: {numero_pc}')
        #         feedback = input('O palpite do computador é (maior, menor ou correto): ')

        # while feedback == 'menor':
        #     piso = numero_pc
        #     numero_pc = random.randint(piso, teto)
        #     print(f'Computador: {numero_pc}')
        #     feedback = input('O palpite do computador é (maior, menor ou correto): ')

        #     if feedback == 'correto':
        #         print(palpite_certo)
        #         break

        #     elif feedback == 'maior':
        #         teto = numero_pc
        #         numero_pc = random.randint(piso, teto)
        #         print(f'Computador: {numero_pc}')
        #         feedback = input('O palpite do computador é (maior, menor ou correto): ')

        #     elif feedback == 'menor':
        #         piso = numero_pc
        #         numero_pc = random.randint(piso, teto)
        #         print(f'Computador: {numero_pc}')
        #         feedback = input('O palpite do computador é (maior, menor ou correto): ')

    if feedback == 'correto':
        print(palpite_certo)
        break
