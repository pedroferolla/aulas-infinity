# EXERCÍCIOS DE FIXAÇÃO - PARTE1/2
# Operadores lógicos

# Para os exercícios 5 a 10, faça com base no código a seguir:
    # condicao_1 = 10 == 10
    # condicao_2 = 15 != 15

    # print(condicao_1 and condicao_2)

# 8 - Peça ao usuário para digitar um número e verifique se ele está entre 10 e 20.
    # Não utilize o if.

# RESULTADO ESPERADO:
    # Digite um número: 12
    # True

num = int(input('Digite um número: '))

verificacao = num >= 10 and num <= 20

print(verificacao)
