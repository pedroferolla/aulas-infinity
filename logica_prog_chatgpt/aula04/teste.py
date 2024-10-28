for num in range(1,10):
    if num % 2 == 0:
        print(f'Número par encontrado: {num}, interrompendo o laço.')
        break
    else:
        print(f'{num} é ímpar, continuando.')
else:
    print('Todos os números foram ímpares.')
