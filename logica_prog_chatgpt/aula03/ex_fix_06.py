# EXERCÍCIOS DE FIXAÇÃO

# 6 - Peça ao usuário para digitar um número e exiba a tabuada desse número de 1 a 10.

# RESULTADO ESPERADO:
    # Digite um número para exibir a tabuada: 7
    # 7 x 1 = 7
    # 7 x 2 = 14
    # 7 x 3 = 21
    # 7 x 4 = 28
    # 7 x 5 = 35
    # 7 x 6 = 42
    # 7 x 7 = 49
    # 7 x 8 = 56
    # 7 x 9 = 63
    # 7 x 10 = 70

num = 7
fator = 0

while fator < 10:
    fator += 1
    print(f'{num} x {fator} = {num * fator}')
