# ATIVIDADE PRÁTICA

# Atividade 06:
    # Soma de números positivos:
        # Escreva um programa que solicite números ao usuário até que ele digite um número negativo.
        # Some apenas os números positivos inseridos.

# TENTATIVA 1:
# numero1 = float(input('Digite o primeiro número: '))
# numero2 = float(input('Digite o segundo número: '))
# soma = numero1 + numero2

# while numero1 >= 0 and numero2 >= 0:
#     print(f'Soma = {soma}')
#     if numero1 < 0 or numero2 < 0:
#         print('A soma só é feita entre números positivos. Tente novamente.')


# DÚVIDA: DÚVIDA NO ENTENDIMENTO DA QUESTÃO.
        # CASO SEJA FEITA A SOMA APENAS ENTRE 2 NÚMEROS, QUAL A RELAÇÃO COM O LOOP? O PROGRAMA TEM QUE SER RODADO MANUALMENTE, NO CASO...



# TENTATIVA 2:
# numero = int(input('Digite um número: '))

# while numero >= 0:
#     numero += numero
#     print(f'Soma dos números digitados: {numero += numero} ')



# TENTATIVA 3
# numero = int(input('Digite um número: '))
# numero += numero

# while numero >= 0:
#     print(f'Soma = {numero}')
#     if numero < 0:
#         print(f'Soma feita apenas entre os números positivos: {numero}')



# TENTATIVA 4:
# numero = int(input('Digite um número: '))
# proximo_numero = int(input('Digite o próximo número: '))

# while numero >= 0 and proximo_numero >= 0:
#     print



# TENTATIVA 5:
numero = int(input('Digite um número: '))
proximo = int()

while proximo >= 0:
    proximo = int(input('Digite o próximo número: '))
    if proximo >= 0:
        numero += proximo
    print(f'Soma = {numero}')
