# Peça ao usuário para inserir seu nome e o número de telefone.
# Imprima uma mensagem usando f-string com essas informações, por exemplo:

# Resultado esperado:
    # Digite seu nome: Carol
    # Digite seu número de telefone: 123456789
    # ----------------------------------------
    # Carol, seu número de telefone é 123456789.

nome = input('Digite seu nome: ')
telefone = input('Digite seu número de telefone: ')

print(f'{nome}, seu número de telefone é {telefone}.')