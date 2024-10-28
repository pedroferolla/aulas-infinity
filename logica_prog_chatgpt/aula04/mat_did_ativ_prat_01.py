# ATIVIDADE PRÁTICA

# Atividade 01:
    # Tabuada de um número:
        # Faça um programa que solicite um número ao usuário e use um laço For para exibir a tabuada
        # desse número (de 1 a 10).

num = int(input('Digite um número para exibir sua tabuada de 10: '))

for i in range(10):
    i += 1
    print(f'{i} x {num} = {i * num}')
