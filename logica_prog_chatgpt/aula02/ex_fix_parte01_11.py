# EXERCÍCIOS DE FIXAÇÃO - PARTE1/2
# Operadores lógicos

# 11 - Peça ao usuário para digitar uma determinada palavra que está contida na frase "Aprender Python está sendo muito legal.".
    # Retorne True se a palavra estiver e False se não estiver.
    # Não utilize o if.

# RESULTADO ESPERADO:
    # Digite uma palavra para verificar na frase: Python
    # True

palavra = input('Digite uma palavra que está contida na frase "Aprender Python está sendo muito legal.": ')
frase = 'Aprender Python está sendo muito legal.'

verificacao = palavra in frase

print(verificacao)
