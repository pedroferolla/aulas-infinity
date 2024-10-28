# ATIVIDADE PRÁTICA

# Atividade 04:
    # Contagem regressiva:
        # Desenvolva um programa que use um laço While para exibir uma contagem regressiva de 10 até 1.
        # Em seguida, exiba "Feliz Ano Novo!".

contagem = 10

while contagem >= 1:
    print(contagem)
    contagem -= 1
    if contagem < 1:
        print('Feliz Ano Novo!')
