# APRENDIZAGEM

# 8 - Usando o dicionário 'frutas = {'maçã': 5, 'banana': 3, 'laranja': 0}', escreva um código que remova as frutas com 
    # quantidade igual a 0 e imprima o dicionário resultante.

frutas = {'maçã': 5, 'banana': 3, 'laranja': 0}

for chave, valor in frutas.items():
    if valor == 0:
        del frutas[chave]   # <---- Até a remoção Ok, mas o loop continua, dando erro, uma vez que o dic foi modificado.

print(frutas)
