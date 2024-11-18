# EXERCÍCIOS DE FIXAÇÃO - PARTE 2/2

# 4 - Crie um dicionário onde as chaves são nomes de alunos e os valores são listas de notas.
    # Classifique os alunos em 'Aprovado' (média >= 7) e 'Reprovado' (média < 7).
    # Exiba duas listas: uma para alunos aprovados e outra para alunos reprovados.

notas_alunos = {
    "Ana": [8.5, 9.0, 7.5],
    "Pedro": [5.5, 6.0, 7.0],
    "Maria": [7.0, 7.5, 6.0]
}

medias_alunos = {}
aprovado = {}
reprovado = {}

aprovado_lista = []
reprovado_lista = []

for chave, valor in notas_alunos.items():
    dividendo = 0
    divisor = 0
    media = 0

    for i in valor:
        dividendo += i
        divisor +=1
    
    media = dividendo / divisor
    
    medias_alunos[chave] = media

for chave, valor in medias_alunos.items():
    if valor >= 7:
        aprovado[chave] = valor
        aprovado_lista.append(chave)
    else:
        reprovado[chave] = valor
        reprovado_lista.append(chave)

print(medias_alunos)

print(f'\nAprovados: {aprovado_lista}')
print(f'Reprovados: {reprovado_lista}')

for chave, valor in aprovado.items():
    print(f'\n{chave}: {valor:.2f} - Aprovado(a)')

for chave, valor in reprovado.items():
    print(f'{chave}: {valor:.2f} - Reprovado(a)')
