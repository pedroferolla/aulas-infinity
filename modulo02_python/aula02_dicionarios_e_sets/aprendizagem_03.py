# APRENDIZAGEM

# 3 - Usando o dicionário 'idades = {'Alice': 30, 'Bob': 25, 'Carol': 22}', escreva um loop que imprima cada chave e 
    # seu respectivo valor no formato: 'Nome: Idade'.

idades = {
    'Alice': 30,
    'Bob': 25,
    'Carol': 22
}

for chave, valor in idades.items():
    print(f'{chave}: {valor}')
