# EXERCÍCIOS DE FIXAÇÃO

# 1 - Crie um programa que pergunte se a pessoa quer continuar no programa.
    # Caso ela digite sim, pergunte novamente.
        # s = Sim
        # n = Não

# RESULTADO ESPERADO:
    # Quer continuar? s
    # Quer continuar? s
    # Quer continuar? n

    # Programa encerrado.

resposta = input('Você quer continuar no programa? (Sim ou Não): ')
s = 'Sim'
n = 'Não'

while resposta != n:
    resposta = input('Você quer continuar no programa? (Sim ou Não): ')

print('Programa encerrado')
