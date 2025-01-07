# ATIVIDADE PRÁTICA 4

# Crie uma função que receba uma lista de strings e retorne uma nova lista contendo apenas as strings palíndromos.

lista = ['ovo', 'carro', 'pipa', 'elefante', 'mirim', 'bola', 'arara', 'colher', 'radar']

def retorna_palindromos(x = list):
    lista_palindromos = []

    for string in lista:
        if string == ''.join(reversed(string)):
            lista_palindromos.append(string)

    return lista_palindromos

def retorna_palindromos_2(x = list):
    lista_palindromos_2 = []

    for string in lista:
        if string == string[::-1]:
            lista_palindromos_2.append(string)

    return lista_palindromos_2



print(retorna_palindromos(lista))

print(retorna_palindromos_2(lista))
