# APRENDIZAGEM

# 5 - Usando o dicionário 'notas = {'Ana': 8, 'Pedro': 5, 'Luiza': 9, 'João': 4}', crie um novo dicionário contendo 
    # apenas os alunos com notas maiores ou iguais a 7.
    # Imprima o novo dicionário.

notas = {'Ana': 8, 'Pedro': 5, 'Luiza': 9, 'João': 4}
novo_dicionario = {}

for chave, valor in notas.items():
    if valor >= 7:
        novo_dicionario[chave] = valor
    
print(novo_dicionario)
