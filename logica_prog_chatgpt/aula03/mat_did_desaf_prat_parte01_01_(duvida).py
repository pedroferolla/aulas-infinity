# DESAFIOS PRÁTICOS

# Instruções:
    # 1 - Soma de números pares:
        # Crie um programa que use um laço While para somar todos os números pares de 1 a 100 e exiba o resultado.

# Benefícios: praticar o uso de operadores aritméticos em Python e entender como realizar cálculos matemáticos
            # básicos com variáveis.

soma = 0
num = 1

# while num <= 100:
#     soma += num
#     num += 2

#     print(soma)

while num <= 100:
    num += 1

    if num % 2 == 0:
        soma += num     # <------- Como iniciar a soma a partir do 2 (2 + 4 = 6)?
        num += 1

        print(soma)
