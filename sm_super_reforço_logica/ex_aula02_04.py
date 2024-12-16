# 13. Faça um programa que peça ao usuário um texto e retorne, quantos caracteres o texto tem, 
    # o número de vogais no texto e o número de palavras.

texto_usuario = input('Digite o texto: ')

vogais = ['a', 'e', 'i', 'o', 'u']

# Número de caracteres:
numero_caracteres = len(texto_usuario)
print(f'Número de caracteres no texto: {numero_caracteres}')


# Número de vogais:
numero_vogais = 0

for caractere in texto_usuario:
    if caractere in vogais:
        numero_vogais += 1

print(f'Número de vogais no texto: {numero_vogais}')


# Número de palavras:
lista = []
nova_string = ''

for caractere in texto_usuario:
    if caractere != ' ':
        nova_string += caractere
    else:
        lista.append(nova_string)
        nova_string = ''
lista.append(nova_string)

print(f'Número de palavras: {len(lista)}')




# Gabarito:
frase = input('Digite a frase: ')

qnt_caracter = 0
qnt_vogal = 0

for caracter in frase:
    qnt_caracter += 1

    if caracter.lower() in 'aeiou':
        qnt_vogal += 1


qnt_palavras = len(frase.split(' '))

print(f'Quantidade de caracteres: {qnt_caracter}')
print(f'Quantidade de vogais: {qnt_vogal}')
print(f'Quantidade palavras: {qnt_palavras}')
