maior_numero = None
menor_numero = ''

input('Digite um número: ')

while True:
    numero_usuario = input("Digite o próximo número ('fim' para terminar): ")

    if numero_usuario == 'fim':
        break

    else:
        try:
            numero_usuario = int(numero_usuario)
        except:
            print('O valor digitado é inválido.')
            continue    

        if  maior_numero is None or numero_usuario > maior_numero:
            maior_numero = numero_usuario

        if  menor_numero == '' or numero_usuario < menor_numero:
            menor_numero = numero_usuario

print(f'O maior número é: {maior_numero}')
print(f'O menor número é: {menor_numero}')



# lista = []

# input('Digite um número: ')

# while True:
#     numero_usuario = input("Digite o próximo número ('fim' para terminar): ")

    # if int(numero_usuario) > int(maior_numero):
    #     lista.pop(-1)
    #     lista[-1] = maior_numero

    # elif int(numero_usuario) < int(menor_numero):