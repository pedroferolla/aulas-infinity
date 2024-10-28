# Prova Estrutura de repetição: FOR

# Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo 
# determinado pelo usuário.

# O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do 
# intervalo (inclusive).

# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares.

# Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo,
# caso seja o caso.

# Ao final, exiba a soma dos números pares encontrados.

soma = 0
num1 = int(input('Digite o primeiro número inteiro para o início do intervalo: '))
num2 = int(input('Digite o segundo número inteiro para o fim do intervalo: '))

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        soma += i

    if i == num2:
        print(f'A soma dos números pares encontrados é: {soma}')
        break

else:
    print('Não há números pares no intervalo.')
