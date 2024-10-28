# ATIVIDADE PRÁTICA

# Atividade 07:
    # Verificação de caracteres em uma string:
        # - Crie um programa que peça ao usuário uma frase e um caractere.
        # - Use o operador de associação in para verificar se o caractere está presente na frase.

frase = input('Insira uma frase: ')
caractere = input('Insira um caractere: ')

resultado = caractere in frase
print(resultado)