# DESAFIOS PRÁTICOS

# Instruções:
    # 4 - Sequência de Collatz:
        # Crie um programa que solicite um número ao usuário e use um laço While para gerar e exibir a Sequência de
        # Collatz até chegar ao número 1.

# Benefícios: praticar o uso de operadores aritméticos em Python e entender como realizar cálculos matemáticos
            # básicos com variáveis.

num = int(input('Digite um número para sua sequência de Collatz: '))

# num = 123   <------------------ Variável de controle

while num > 1:
    if num % 2 != 0:
        num = 3 * num + 1
        num /= 2
        print(num)
    else:
        num /= 2
        print(num)
