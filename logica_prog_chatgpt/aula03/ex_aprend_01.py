# EXERCÍCIOS DE APRENDIZAGEM

# 1 - Crie um programa que leia duas notas de alunos e tire a média delas.
    # O programa só deve aceitar notas entre 0 e 10.

# RESULTADO ESPERADO:
    # Digite a primeira nota (entre 0 e 10): 7.5
    # Digite a segunda nota (entre 0 e 10): 8.3
    # ------------------------------------------
    # A média das notas 7.5 e 8.3 é: 7.9

nota1 = float(input('Digite a primeira nota (entre 0 e 10): '))
nota2 = float(input('Digite a segunda nota (entre 0 e 10): '))

media = (nota1 + nota2) / 2

while nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print('Nota inválida. Nota deve ser entre 0 e 10. Tente novamente.')
    nota1 = float(input('Digite a primeira nota (entre 0 e 10): '))
    nota2 = float(input('Digite a segunda nota (entre 0 e 10): '))

print(f'A média das notas {nota1} e {nota2} é: {media}')
