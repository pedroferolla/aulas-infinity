# EXERCÍCIOS DE FIXAÇÃO - PARTE2/2

# 6 - Escreva um programa que verifica a idade de uma pessoa e imprime em qual faixa etária ela se encontra:
    # a. CRIANÇA: até 11 anos
    # b. ADOLESCENTE: de 12 a 17 anos
    # c. ADULTO: de 18 a 59 anos
    # d. IDOSO: maiores de 60 anos

idade = int(input('Digite sua idade: '))

if idade <= 11:
    print('CRIANÇA')
elif idade <= 17:
    print('ADOLESCENTE')
elif idade <= 59:
    print('ADULTO')
else:
    print('IDOSO')
