# ATIVIDADE PRÁTICA 2

# Faça um programa que leia 3 números e informe o maior número e o menor.

indice_num_usuario = 1
lista = []

numero = int(input(f'Digite o {indice_num_usuario}º número: '))
lista.append(numero)

while indice_num_usuario < 3:
    indice_num_usuario += 1
    novo_numero = int(input(f'Digite o {indice_num_usuario}º número: '))
    
    lista.append(novo_numero)

print(lista)

if lista[0] < lista[1] and lista[0] < lista[2]:
    print(f'\nMenor número: {lista[0]}')
elif lista[0] > lista[1] and lista[0] > lista[2]:
    print(f'\nMaior número: {lista[0]}')

if lista[1] < lista[0] and lista[1] < lista[2]:
    print(f'\nMenor número: {lista[1]}')
elif lista[1] > lista[0] and lista[1] > lista[2]:
    print(f'\nMaior número: {lista[1]}')

if lista[2] < lista[0] and lista[2] < lista[1]:
    print(f'\nMenor número: {lista[2]}')
elif lista[2] > lista[0] and lista[2] > lista[1]:
    print(f'\nMaior número: {lista[2]}')
