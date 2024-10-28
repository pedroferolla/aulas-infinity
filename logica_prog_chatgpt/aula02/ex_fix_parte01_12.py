# EXERCÍCIOS DE FIXAÇÃO - PARTE1/2
# Operadores lógicos

# 12 - Solicite ao usuário para digitar seu nome de usuário desejado.
    # Retorne True se o nome tiver @ e False se não tiver.
    # Não utilize o if.

# RESULTADO ESPERADO:
    # Digite seu nome de usuário desejado: user@example.com
    # True

usuario = input('Digite seu nome de usuário desejado: ')

retorno = '@' in usuario

print(retorno)
