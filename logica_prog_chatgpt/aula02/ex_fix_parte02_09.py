# EXERCÍCIOS DE FIXAÇÃO - PARTE2/2

# 9 - Faça um programa que solicita ao usuário que informe em qual turno ele estuda, usando as opções:
        # M para Matutino
        # V para Vespertino
        # N para Noturno
    # Com base na escolha do usuário, o programa imprimirá a saudação apropriada:
        # "Bom dia!"
        # "Boa tarde!"
        # "Boa noite!"
        # Ou informará "Valor inválido!", caso a entrada não seja uma das opções esperadas.

turno = input('Informe em qual turno você estuda (M, V ou N): ')

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido!')
