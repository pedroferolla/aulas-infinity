# DESAFIOS PRÁTICOS

# Instruções:
    # 3 - Sequência de Fibonacci:
        # Faça um programa que use um laço While para exibir os primeiros 20 termos da sequência de Fibonacci.

# Benefícios: praticar o uso de operadores aritméticos em Python e entender como realizar cálculos matemáticos
            # básicos com variáveis.

termo_inicial = 0
termo_limite = 20

f1 = 0
f2 = 1

#soma = f1 + f2

# while termo_inicial <= termo_limite:
#     soma = print(f'{f1} + {f2} = {f1 + f2}')  <----- Esta variável resulta em STRING, por isso o programa não calcula!
#     f1 += 1
#     f2 += f1
#     termo_inicial += 1

#     if termo_inicial == termo_limite:
#         break

while termo_inicial <= termo_limite:
    soma = f1 + f2
    print(f'{f1} + {f2} = {soma}')
    
    f1 = f2
    f2 = soma

    termo_inicial += 1

    if termo_inicial == termo_limite:
        break

# CONFERIR SE O ALGORÍTMO ATENDE AO ENUNCIADO.
