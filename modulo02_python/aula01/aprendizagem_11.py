# APRENDIZAGEM

# 11 - Faça um programa que peça as quatro notas de 3 alunos, calcule e armazene num vetor a média de cada aluno, 
    # imprima o número de alunos com média maior ou igual a 7.0.

aluno1 = []
aluno2 = []
aluno3 = []

numerador_nota = 0
print('\nAluno 1:')
for i in range(0,4):
    numerador_nota += 1
    aluno1.append(int(input(f'Digite a {numerador_nota}ª nota: ')))

media1 = (aluno1[0] + aluno1[1] + aluno1[2] + aluno1[3]) / 4


numerador_nota = 0
print('\nAluno 2:')
for i in range(0,4):
    numerador_nota += 1
    aluno2.append(int(input(f'Digite a {numerador_nota}ª nota: ')))

media2 = (aluno2[0] + aluno2[1] + aluno2[2] + aluno2[3]) / 4


numerador_nota = 0
print('\nAluno 3:')
for i in range(0,4):
    numerador_nota += 1
    aluno3.append(int(input(f'Digite a {numerador_nota}ª nota: ')))

media3 = (aluno3[0] + aluno3[1] + aluno3[2] + aluno3[3]) / 4


media_alunos = [media1, media2, media3]
media_aprovados = []

for i in media_alunos:
    if i >= 7:
        media_aprovados.append(i)

print(media_alunos)
print(f'Número de alunos com média 7 ou maior: {len(media_aprovados)}')
