# DESAFIOS

# 2 - Faça um programa que mostre os n termos da série a seguir e imprima no final a soma da série:
    # s = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m

# RESULTADO ESPERADO:
    # Digite o número de termos da série que deseja calcular: 5
    # ---------------------------------------------------------
    # Os primeiros 5 termos da série são:
    # 1/1 = 1.0000
    # 2/3 = 0.6667
    # 3/5 = 0.6000
    # 4/7 = 0.5714
    # 5/9 = 0.5556

    # A soma da série é: 3.3937

num1 = 1
num2 = 1


num_usuario = int(input('Digite o número de termos da série que deseja calcular: '))
termo = 0
soma = 0

print(f'\nOs primeiros {num_usuario} termos da série são:')

while termo <= num_usuario:
    divisao = float(num1 / num2)
    print(f'{num1}/{num2} = {divisao:.4f}')
    num1 += 1
    num2 += 2
    soma += divisao
    termo += 1

    if termo == num_usuario:
        print(f'\nA soma da série é: {soma:.4f}')
        break
