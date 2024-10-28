# DESAFIOS

# 2 - Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
    # Observando os termos no plural, a colocação do "e", da vírgula, entre outros.

# EXEMPLOS:
    # a. 326 = 3 centenas, 2 dezenas e 6 unidades
    # b. 12 = 1 dezena e 2 unidades

# Testar com os números : 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16.

numero = int(input('Digite um número inteiro menor que 1000: '))

if numero <= 0:
    print('Digite um número inteiro menor que 1000 válido!')
else:
    centenas = numero // 100
    numero = numero % 100

    dezenas = numero // 10
    numero = numero % 10

    unidades = numero

resultado = ''
if centenas > 0:
    if centenas == 1:
        resultado += f'{centenas} centena'
    else:
        resultado += f'{centenas} centenas'

if dezenas > 0:
    if centenas > 0:
        resultado += ', '
    if dezenas == 1:
        resultado += f'{dezenas} dezena'
    else:
        resultado += f'{dezenas} dezenas'

if unidades > 0:
    if centenas > 0 or dezenas > 0:
        resultado += ' e '
    if unidades == 1:
        resultado += f'{unidades} unidade.'
    else:
        resultado += f'{unidades} unidades.'

print(resultado)


# GABARITO:
# Solicita ao usuário que digite um número inteiro menor que 100:
# numero = int(input('Digite um número inteiro menor que 100: '))

# Verifica se o número está dentro do intervalo válido:
# if numero >= 1000:
    # print('Número deve ser menor que 1000.')
# else:
    # Calcula centenas, dezenas e unidades:
    # centenas = numero // 100
    # dezenas = (numero % 100) // 10
    # unidades = numero % 10

# Constrói a string de resultado com base nas quantidades
# resultado = ''
# if centenas > 0:
#     if centenas == 1:
#         resultado += f'{centenas} centena'
#     else:
#         resultado += f'{centenas} centenas'

# if dezenas > 0:
#     if centenas > 0:
#         resultado += ', '
#     if dezenas == 1:
#         resultado += f'{dezenas} dezena'
#     else:
#         resultado += f'{dezenas} dezenas'

# if unidades > 0:
#     if centenas > 0 or dezenas > 0:
#         resultado += ' e '
#     if unidades == 1:
#         resultado += f'{unidades} unidade.'
#     else:
#         resultado += f'{unidades} unidades.'

# Imprime o resultado final:
# print(resultado)
