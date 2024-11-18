# APRENDIZAGEM

# 6 - Dada a lista 'itens = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']', crie um dicionário que 
    # conte quantas vezes cada fruta aparece na lista.
    # Imprima o dicionário resultante.

itens = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']
dicionario = {}

qnt_maca = 0
qnt_banana = 0
qnt_laranja = 0

for fruta in itens:
    if fruta == 'maçã':
        qnt_maca += 1
        dicionario['maçã'] = qnt_maca
    elif fruta == 'banana':
        qnt_banana += 1
        dicionario['banana'] = qnt_banana
    else:
        qnt_laranja += 1
        dicionario['laranja'] = qnt_laranja
    
print(dicionario)


# CONFERIR SE O CÓDIGO ATENDE AO ENUNCIADO, UMA VEZ QUE FOI NECESSÁRIO SABER QUAIS DIFERENTES ITENS TINHAM NA LISTA.
