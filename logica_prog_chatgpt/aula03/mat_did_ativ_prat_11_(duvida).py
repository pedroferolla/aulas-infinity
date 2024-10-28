# ATIVIDADE PRÁTICA

# Atividade 11:
    # Entrada válida:
        # Crie um programa que solicite ao usuário um número entre 1 e 10.
        # Continue pedindo até que o usuário forneça um valor válido.

num = int(input('Digite um número entre 1 e 10: '))

# if num < 1 or num > 10:
#     while num < 1 or num > 10:
#         num = int(input('Número inválido! Tente novamente: '))
#         if num >= 1 and num <= 10:
#             print('Número válido!')
#             break
# else:
#     print('Número válido!')

# OBS: VERIFICAR SE O ALGORÍTIMO ESTÁ CORRETO!


while num < 1 or num > 10:
    num = int(input('Número inválido. Digite um número entre 1 e 10: '))

print('Número válido!')
