# EXERCÍCIOS DE FIXAÇÃO
# Kwargs

# 1 - Crie uma função chamada 'imprimir_kwargs', que aceite um número variável de argumentos nomeados e imprima cada um deles 
    # no formato 'chave: valor'.

    # Input:
    # imprimir_kwargs(nome = 'João', idade = 30, cidade = 'São Paulo')

    # Resultado esperado:
    # nome: João
    # idade: 30
    # cidade: São Paulo

def imprimir_kwargs(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

imprimir_kwargs(nome = 'João', idade = 30, cidade = 'São Paulo')
