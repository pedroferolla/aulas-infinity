# EXERCÍCIOS DE APRENDIZAGEM

# 3 - Crie um programa que leia vários números inteiros pelo teclado.
    # O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
    # No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999).

# RESULTADO ESPERADO:
    # Digite um número inteiro (999 para parar): 3
    # Digite um número inteiro (999 para parar): 7
    # Digite um número inteiro (999 para parar): 12
    # Digite um número inteiro (999 para parar): 999
    # ----------------------------------------------
    # Total de números digitados: 3
    # Soma dos números digitados: 22

# num = int(input('Digite um número inteiro (999 para parar): '))
contagem = 0
soma = 0
# parar = '999'

# while num != parar:
#     num = int(input('Digite um número inteiro (999 para parar): '))
#     contagem += 1
#     soma += num

#     if num == parar:
#         print(f'Total de números digitados: {contagem}')
#         print(f'Soma dos números digitados: {soma}')

while True:
    num = int(input('Digite um número inteiro (999 para parar): '))
    contagem += 1
    soma += num

    if num == 999:
        contagem -= 1
        soma -= 999
        print(f'Total de números digitados: {contagem}')
        print(f'Soma dos números digitados: {soma}')
        break
