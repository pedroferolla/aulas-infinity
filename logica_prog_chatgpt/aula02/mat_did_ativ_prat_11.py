# ATIVIDADE PRÁTICA

# Atividade 11:
    # Verificar Par ou Ímpar e Positivo ou Negativo:
        # Escreva um programa que peça um número e use if para verificar se ele é par ou ímpar e também se é positivo ou negativo.

numero = int(input('Insira um número: '))

if numero % 2 == 0 and numero > 0:
    print('Número par e positivo.')
elif numero % 2 == 0 and numero <0:
    print('Número par e negativo.')
elif numero % 2 != 0 and numero > 0:
    print('Número ímpar e positivo.')
else:
    print('Número ímpar e negativo.')
