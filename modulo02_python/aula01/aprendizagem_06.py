# APRENDIZAGEM

# 6 - Crie uma função que recebe uma lista de números e retorna a média dos números presentes na lista.

    # numeros = [10, 20, 30, 40, 50]

numeros = [10, 20, 30, 40, 50]

dividendo = 0
divisor = 0

for i in numeros:
    dividendo += i
    divisor += 1

media = dividendo / divisor

print(f'Média dos números da lista: {media}')
