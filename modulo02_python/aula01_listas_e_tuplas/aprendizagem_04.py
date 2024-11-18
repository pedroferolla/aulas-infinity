# APRENDIZAGEM

# 4 - Dada a lista ['maçã', 'banana', 'cereja'], crie uma nova lista onde cada elemento seja a concatenação do 
    # nome da fruta com o índice da lista.

    # lista_nova = ['maçã_0', 'banana_1', 'cereja_2']

lista = ['maçã', 'banana', 'cereja']
lista_nova = []

for i in lista:
    indice = lista.index(i)
    lista_nova.append(f'{i}_{indice}')

print(lista_nova)
