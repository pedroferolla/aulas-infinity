# ATIVIDADE PRÁTICA 3

# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de 
# números ímpares.

indice_num_usuario = 1
lista = []
lista_pares = []
lista_impares = []

numero = int(input(f'Digite o {indice_num_usuario}º número: '))
lista.append(numero)

while indice_num_usuario < 10:
    indice_num_usuario += 1
    novo_numero = int(input(f'Digite o {indice_num_usuario}º número: '))
    
    lista.append(novo_numero)

print(lista)

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    elif i % 2 != 0:
        lista_impares.append(i)

print(f'Quantidade de números pares: {len(lista_pares)}')
print(f'Quantidade de números ímpares: {len(lista_impares)}')
