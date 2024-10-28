# APRENDIZAGEM

# 5 - Dada uma lista de strings, crie uma nova lista onde cada string seja convertida para maiúsculas e 
    # as strings que começarem com 'A' sejam removidas.

# Para converter para maíscula é só utilizar:
    # nome_string.upper()

lista = ['maçã', 'acerola', 'banana', 'cereja', 'abacaxi']
nova_lista = []

for i in lista:
    if i[0] == 'a':
        continue

    nova_lista.append(i.upper())

print(nova_lista)
