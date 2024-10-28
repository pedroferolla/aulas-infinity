# EXERCÍCIOS DE FIXAÇÃO - PARTE1/2
# Operadores lógicos

# 13 - Peça ao usuário para inserir dois números inteiros e exiba o resto da divisão do primeiro pelo segundo.

# RESULTADO ESPERADO:
    # Digite o primeiro número inteiro: 15
    # Digite o segundo número inteiro: 4
    # 15 % 4 = 3

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

resto = num1 % num2

print(f'{num1} % {num2} = {resto}')
