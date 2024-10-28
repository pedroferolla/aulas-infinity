# EXERCÍCIOS DE FIXAÇÃO - PARTE1/2
# Comparação

# Para os exercícios 5 a 10, faça com base no código a seguir:
    # condicao_1 = 10 == 10
    # condicao_2 = 15 != 15

    # print(condicao_1 and condicao_2)

# 5 - Peça ao usuário para digitar dois números e teste se eles são iguais.
    # Mostre True se forem iguais e False se forem diferentes.
    # Não utilize o if para isso, somente faça a comparação.

# RESULTADO ESPERADO:
    # Digite o primeiro número: 10
    # Digite o segundo número: 10
    # True

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

numeros_iguais = num1 == num2

print(numeros_iguais)
