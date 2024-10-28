# EXERCÍCIOS DE FIXAÇÃO

# 5 - Solicite que o usuário digite números inteiros positivos e exiba a soma desses números.
    # Encerre o programa quando o usuário digitar um número negativo.

# RESULTADO ESPERADO:
    # Digite um número positivo (digite um número negativo para encerrar): 10
    # Digite um número positivo (digite um número negativo para encerrar): 15
    # Digite um número positivo (digite um número negativo para encerrar): 8
    # Digite um número positivo (digite um número negativo para encerrar): -3

    # Soma dos números positivos digitados: 33

num = int(input('Digite um número positivo (digite um número negativo para encerrar): '))
soma = 0

while num >= 0:
    soma += num
    num = int(input('Digite um número positivo (digite um número negativo para encerrar): '))

print(f'Soma dos números positivos digitados: {soma}')
