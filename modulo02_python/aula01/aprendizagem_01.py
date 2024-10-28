# APRENDIZAGEM

# 1 - Dada a lista de strings abaixo, crie uma nova lista contendo as strings que têm mais de 4 caracteres.

    # strings = ['sol', 'lua', 'estrela', 'galáxia']

strings = ['sol', 'lua', 'estrela', 'galáxia']

nova_lista = []

for i in strings:
    if len(i) > 4:
        nova_lista.append(i)

print(nova_lista)
