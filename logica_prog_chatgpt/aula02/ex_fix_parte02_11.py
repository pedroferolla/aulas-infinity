# EXERCÍCIOS DE FIXAÇÃO - PARTE2/2

# 11 - Escreva um programa que verifica se a idade digitada pelo usuário indica que ele deve votar (idade >= 18 anos) ou não.
    # Imprima a mensagem correspondente:
        # a. Menor de 16 anos: "Não vota."
        # b. Entre 18 e 70: "Voto obrigatório."
        # c. 16, 17 ou maior de 70 anos: "Voto facultativo."

idade = int(input('Digite sua idade: '))

if idade < 16:
    print('Não vota.')
elif idade >= 18 and idade <= 70:
    print('Voto obrigatório.')
else:
    print('Voto facultativo.')
