# ATIVIDADE PRÁTICA 9

# Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.

dicionario = {
    'Bud': 10,
    'Pirata': 18
}

for i in dicionario.items():
    print(i)

for chave, valor in dicionario.items():
    print(f'Nome: {chave} - Idade: {valor}')
