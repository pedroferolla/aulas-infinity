# DESAFIOS PRÁTICOS

# Instruções:
    # 4 - Fatorial de um número:
        # Desenvolva um programa que solicite um número ao usuário e use um laço While para calcular o fatorial desse número.

# Benefícios: praticar o uso de operadores aritméticos em Python e entender como realizar cálculos matemáticos
            # básicos com variáveis.

# num = int(input('Digite um número inteiro para calcular seu fatorial: '))

fator = 0
num = int(input('Digite um número para calcular seu fatorial: '))

x = 1
y = 1

# while fator <= num:
#     fatorial = x * y
#     print(f'{x} x {y} = {fatorial}')

#     x = fatorial
#     y += 1
#     fatorial *= y

#     fator += 1

#     if fator == num:
#         break

while fator <= num:
    y += 1
    fatorial = x * y
    print(f'{x} x {y} = {fatorial}')

    x = fatorial
    fatorial *= y

    fator += 1

    if fator == num:
        break

# CONFERIR OS ALGORITMOS, POIS OS DOIS NÃO ESTÃO 100%.
