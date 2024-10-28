# EXERCÍCIOS DE FIXAÇÃO

# 4 - Escreva um programa que inicie uma contagem regressiva a partir de um número fornecido pelo usuário até zero,
    # exibindo cada número na tela.

# RESULTADO ESPERADO:
    # Digite um número para iniciar a contagem regressiva: 5
    # 5
    # 4
    # 3
    # 2
    # 1
    # 0

num = int(input('Digite um número para iniciar a contagem regressiva: '))

while num >= 0:
    print(num)
    num -= 1
