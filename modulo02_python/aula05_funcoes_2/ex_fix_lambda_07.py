# EXERCÍCIOS DE FIXAÇÃO
# Funções Lambda

# 7 - Crie uma função lambda para substituir todas as ocorrências do caractere 'a' por 'o' em uma string dada.
    # Para isso, utilize o código:
        # texto.replace('texto original', 'texto para substituir')

        # Exemplo:
        # Substitui todas as letras 'a' por letras 'o'.
        # texto.replace('a', 'o')


substituir = lambda texto: texto.replace('a', 'o')

print(substituir('banana'))

