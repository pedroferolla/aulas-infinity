# Crie uma função que recebe uma coleção (lista ou tupla) e retorna o maior valor da coleção:

def retornar_maior_e_menor(colecao: list[int]) -> int:
    maior = colecao[0]

    for numero in colecao:
        if numero > maior:
            maior = numero

    return maior



# LOOP INFINITO:

##################################

# lista = [1,2,3,4,5]

# for nun in lista:
#     print(nun)

#     if not nun % 2:
#         lista.append(nun ** 3)

##################################
