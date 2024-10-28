# EXERCÍCIOS DE FIXAÇÃO - PARTE1/2
# Operadores lógicos

# Para os exercícios 5 a 10, faça com base no código a seguir:
    # condicao_1 = 10 == 10
    # condicao_2 = 15 != 15

    # print(condicao_1 and condicao_2)

# 10 - Peça ao usuário para digitar sua idade e verifique se ela é menor que 18 anos ou maior que 65 anos.
    # Não utilize o if.

# RESULTADO ESPERADO:
    # Digite sua idade: 17
    # True

idade = int(input('Digite sua idade: '))

verificacao = idade < 18 or idade > 65

print(verificacao)
