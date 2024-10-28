# EXERCÍCIOS DE APRENDIZAGEM

# 1 - Escreva um programa que verifica se três números digitados pelo usuário representam os lados de um triângulo equlátero, isósceles ou escaleno.
    # a. EQUILÁTERO: três lados iguais
    # b. ISÓSCELES: dois lados iguais
    # c. ESCALENO: todos os lados são diferentes

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 == num2 == num3:
    print('EQUILÁTERO')
elif num1 == num2 and num1 != num3:
    print('ISÓSCELES')
elif num1 == num3 and num1 != num2:
    print('ISÓSCELES')
elif num2 == num3 and num2 != num1:
    print('ISÓSCELES')
else:
    print('ESCALENO')


# GABARITO:
    # if num1 == num2 == num3:
        # print('EQUILÁTERO')
    # elif num1 != num2 != num3:
        # print('ESCALENO')
    # else:
        # print('ISÓSCELES')
