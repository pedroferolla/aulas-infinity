# DESAFIOS

# 3 - Faça um programa que leia duas notas parciais obtidas por um aluno numa disciplina ao longo do semestre, e calcule sua média.
    # A atribuição de conceitos obedece à tabela abaixo:

    # Média de aproveitamento    Conceito
    # Entre 9.0 e 10.0              A
    # Entre 7.5 e 9.0               B
    # Entre 6.0 e 7.5               C
    # Entre 4.0 e 6.0               D
    # Entre 4.0 e zero              E

    # O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem "APROVADO" se o conceito for A, B ou C, ou "REPROVADO" se o conceito for D ou E.

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 + nota_2) / 2
conceito = 'x'

if media >= 0 and media < 4:
    conceito = 'E'
    
if media >= 4 and media < 6:
    conceito = 'D'

if media >= 6 and media < 7.5:
    conceito = 'C'

if media >= 7.5 and media < 9:
    conceito = 'B'

if media >= 9 and media <= 10:
    conceito = 'A'

if conceito == 'E' or conceito == 'D':
    print(f'Primeira nota: {nota_1}')
    print(f'Segunda nota: {nota_2}')
    print(f'Média: {media:.2f}')
    print(f'Conceito: {conceito}')
    print(f'REPROVADO')
else:
    print(f'Primeira nota: {nota_1}')
    print(f'Segunda nota: {nota_2}')
    print(f'Média: {media:.2f}')
    print(f'Conceito: {conceito}')
    print(f'APROVADO')


# GABARITO:
# Solicita ao usuário que digite as duas notas parciais:
# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))

# Calcula a média das notas:
# media = (nota1 + nota2) / 2

# Determinar o conceito baseado na média:
# if media >= 9.0 and media <= 10.0:
    # conceito = 'A'
# elif media >= 7.5 and media < 9.0:
    # conceito = 'B'
# elif media >= 6.0 and media < 7.5:
    # conceito = 'C'
# elif media >= 4.0 and media < 6.0:
    # conceito = 'D'
# elif media >= 0 and media < 4.0:
    # conceito = 'E'
# else:
    # conceito = 'Conceito indefinido'

# Imprime na tela as notas, a média, o conceito correspondente e a situação do aluno:
# print(f'Nota 1: {nota1}')
# print(f'Nota 2: {nota2}')
# print(f'Média: {media:.1f}')
# print(f'Conceito: {conceito}')

# Verifica se o aluno foi aprovado ou reprovado:
# if conceito in ['A', 'B', 'C']:
    # print('Situação: APROVADO')
# else:
    # print('Situação: REPROVADO')
