# ATIVIDADE PRÁTICA 4

# Faça um programa que peça para 'n' pessoas a sua idade, ao final, o programa deverá verificar se a média de idade da 
# turma varia entre 0 e 25, 26 e 60 e maior que 60, e então dizer se a turma é jovem, adulta ou idosa, conforme a 
# média calculada.

idades = []

while True:
    idade_aluno = int(input('Digite a idade do aluno (0 para finalizar): '))

    if idade_aluno == 0:
        break

    idades.append(idade_aluno)

soma_idades = 0

for idade in idades:
    soma_idades += idade

media = soma_idades / len(idades)

if media <= 25:
    print(f'Média de idade da turma: {media:.0f} - Turma jovem.')
elif media >= 26 and media <= 60:
    print(f'Média de idade da turma: {media:.0f} - Turma adulta.')
else:
    print(f'Média de idade da turma: {media:.0f} - Turma idosa.')
