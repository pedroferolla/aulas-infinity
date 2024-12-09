# EXERCÍCIOS DE FIXAÇÃO
# Args

# 5 - Crie uma função chamada 'contar_palavras', que aceite um número variável de argumentos (strings) e retorne o número 
    # total de palavras em todas as srings fornecidas.

    # Input:
    # contar_palavras('Olá Mundo', 'Como você está hoje?')

    # Resultado esperado:
    # 6

def contar_palavras(*args):
    lista = []
    espacos_lista = 0
    espacos_strings = 0
    
    for i in args:
        lista.append(i)

    for string in lista:
        espacos_lista = len(lista) - 1

        for caractere in string:
            if caractere == ' ':
                espacos_strings += 1

    palavras_contadas = espacos_lista + espacos_strings + 1

    return palavras_contadas

print(contar_palavras('Olá Mundo', 'Como você está hoje?'))


# DUVIDA: como fazer a contagem, da forma correta, de palavras dentro de uma string que contém espaço?
# Comentário do professor: o caminho é exatamente pela contagem de espaços!
