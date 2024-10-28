# DESAFIOS PRÁTICOS

# Instruções:
    # 1 - Números pares em um intervalo:
        # Crie um programa que solicite dois números ao usuário, representando um intervalo.
        # Use um laço While para exibir todos os números pares dentro desse intervalo.

# Benefícios: praticar o uso de operadores aritméticos em Python e entender como realizar cálculos matemáticos
            # básicos com variáveis.

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

# num1 = 5
# num2 = 25

# while num1 <= num2:
    
#     num1 += 1
#     if num1 % 2 == 0:
#         print(num1)
    
while num1 <= num2:
    if num1 % 2 == 0:
        print(num1)
        num1 += 1

    elif num1 % 2 != 0:
        num1 += 1
        print(num1)
        num1 += 1


    if num1 == num2:
        break
