# EXERCÍCIOS DE FIXAÇÃO - PARTE1/2
# Comparação

# Para os exercícios 5 a 10, faça com base no código a seguir:
    # condicao_1 = 10 == 10
    # condicao_2 = 15 != 15

    # print(condicao_1 and condicao_2)

# 6 - Solicite dois números do usuário e exiba True se forem diferentes e False se forem iguais.
    # Não utilize o if para isso, somente faça a comparação.

# RESULTADO ESPERADO:
    # Digite o primeiro número: 15
    # Digite o segundo número: 20
    # True

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

numeros_diferentes = num1 != num2

print(numeros_diferentes)
