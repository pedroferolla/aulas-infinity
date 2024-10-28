# EXERCÍCIOS DE APRENDIZAGEM

# 4 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que é o mais barato.

prod1 = float(input('Insira o preço do produto 1: '))
prod2 = float(input('Insira o preço do produto 2: '))
prod3 = float(input('Insira o preço do produto 3: '))

if prod1 < prod2 and prod1 < prod3:
    print('Você deve comprar o produto 1.')
elif prod2 < prod1 and prod2 < prod3:
    print('Você deve comprar o produto 2.')
else:
    print('Você deve comprar o produto 3.')


# GABARITO:
# prod1 = float(input('Insira o preço do produto 1: '))
# prod2 = float(input('Insira o preço do produto 2: '))
# prod3 = float(input('Insira o preço do produto 3: '))

# Inicializa a variável para armazenar o preço do produto mais barato:
# mais_barato = prod1

# Compara o preço do segundo produto com o produto mais barato atual:
# if prod2 < mais_barato:
#     mais_barato = prod2

# Compara o preço do terceiro produto com o produto mais barato atual:
# if prod3 < mais_barato:
#     mais_barato = prod3

# Imprime o resultado informando qual produto é o mais barato:
# if mais_barato == prod1:
#     print('Você deve comprar o produto 1.')
# elif mais_barato == prod2:
#     print('Você deve comprar o produto 2.')
# else:
#     print('Você deve comprar o produto 3.')
