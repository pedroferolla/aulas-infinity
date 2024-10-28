# DESAFIOS PRÁTICOS

# Instruções:
    # 2 - Contagem regressiva com verificação:
        # Faça um programa que use um laço While para fazer uma contagem regressiva de um número inserido pelo usuário até 0.
        # Durante a contagem, exiba "Número par" para os números pares.

# Benefícios: praticar o uso de operadores aritméticos em Python e entender como realizar cálculos matemáticos
            # básicos com variáveis.

num = int(input('Digite um número: '))

while num > 0:
    if num % 2 == 0:
        print(f'{num} Número par.')

    elif num % 2 != 0:
        print(num)
    
    num -= 1

    if num == 0:
        print(num)
