# Prova Introdução à Inteligência Artificial

# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina.
# O programa deve solicitar o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas.
# Utilize um loop 'for' para iterar sobre os alunos e suas notas.

# Além disso, implemente uma estrutra condicional para verificar se cada aluno foi aprovado ou reprovado, 
# considerando que a média mínima para aprovação é 7,0.
# Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.


alunos_numero = int(input('\nDigite o número de alunos: '))
media_acumulada = 0
media_geral = 0

for aluno in range(1, alunos_numero + 1):
    aluno = input('\nDigite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))

    media_aluno = (nota1 + nota2 + nota3) / 3
    media_acumulada += media_aluno

    if media_aluno >= 7.0:
        print(f'\nAluno: {aluno}')
        print(f'Média: {media_aluno:.2f}')
        print('Aprovado.')
    else:
        print(f'\nAluno: {aluno}')
        print(f'Média: {media_aluno:.2f}')
        print('Reprovado.')

media_geral = media_acumulada / alunos_numero

print(f'\nNúmero de alunos da turma: {alunos_numero}')
print(f'Média geral da turma: {media_geral:.2f}')
