# Escreva um programa que receba uma palavra do usuário e imprima todos os caracteres, exceto as vogais ('a', 'e', 'i', 'o', 'u').

palavra = 'celular'
vogais = 'aeiou'

for letra in palavra:
    if letra in vogais:
        continue
    print(f'{letra} - É consoante')

