# Peça ao usuário para inserir seu nome e sua idade.
# Em seguida, imprima uma mensagem usando f-string com essas informações, por exemplo:

# Resultado esperado:
    # Digite seu nome: Bob
    # Digite sua idade: 25
    # ---------------------
    # Olá Bob! Você tem 25 anos de idade.

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

mensagem = print(f'Olá {nome}! Você tem {idade} anos de idade.')