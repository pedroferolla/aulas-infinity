# EXERCÍCIOS DE APRENDIZAGEM

# 2 - Faça um programa que leia três números e mostre o maior deles.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print(f'O maior número é {num1}.')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é {num2}.')
else:
    print(f'O maior número é {num3}.')


# GABARITO:
    # maior_numero = num1

    # if num2 > maior_numero:
        # maior_numero = num2
    # elif num3 > maior_numero:
        # maior_numero = num3
    
    # print(f'O maior número é: {maior_numero}.')
