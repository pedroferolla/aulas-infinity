# ATIVIDADE PRÁTICA

# Atividade 05:
    # Contagem até o número inserido:
        # Crie um programa que solicite um número ao usuário e use um laço While para contar de 1 até o número inserido.
        # Exiba somente os números ímpares.

numero = int(input('Digite um número: '))
x = 0

while x < numero:
    x += 1
    if x % 2 != 0:
        print(x)
