# EXERCÍCIOS DE FIXAÇÃO - PARTE1/2
# Operadores lógicos

# Para os exercícios 5 a 10, faça com base no código a seguir:
    # condicao_1 = 10 == 10
    # condicao_2 = 15 != 15

    # print(condicao_1 and condicao_2)

# 9 - Peça ao usuário para digitar sua idade e verifique se ela está entre 18 e 65 anos, e se é maior que 21 anos.
    # Não utilize o if.

# RESULTADO ESPERADO:
    # Digite sua idade: 30
    # True

    # Digite sua idade: 19
    # False

idade = int(input('Digite sua idade: '))

entre_18_e_65 = idade >= 18 and idade <=65
maior_que_21 = idade > 21

verificacao = entre_18_e_65 and maior_que_21

print(verificacao)
