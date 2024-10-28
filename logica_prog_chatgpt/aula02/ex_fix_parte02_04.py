# EXERCÍCIOS DE FIXAÇÃO - PARTE2/2

# 4 - Escreva um programa que verifica se a idade digitada pelo usuário indica que ele deve votar (idade >= 18 anos) ou não.
    # Imprima uma mensagem correspondente.

idade = int(input('Digite sua idade: '))

if idade >= 16 and idade < 18 or idade >= 70:
    print('Voto facultativo.')
elif idade >= 18:
    print('Voto obrigatório.')
else:
    print('Não vota.')
