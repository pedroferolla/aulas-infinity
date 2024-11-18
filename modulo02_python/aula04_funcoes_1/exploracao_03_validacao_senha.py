# EXPLORAÇÃO

# 3 - Validação de Senha
    # Crie uma função chamada 'validar_senha', que recebe uma senha e verifica se ela atende aos seguintes critérios:
        # Pelo menos 8 caracteres;
        # Uma vogal;
        # Uma consoante;
        # E um número.

    # Retorne True ou False.

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

lista_senha = []

senha = input('\nDigite sua senha para validação (pelo menos 8 caracteres, uma vogal, uma consoante e um número): ')

criterios = []

def validar_senha(senha: list):
    if len(senha) >= 8:
        criterios.append('V')

    for vogal in vogais:
        if vogal in senha:
            criterios.append('V')
            break
    
    for consoante in consoantes:
        if consoante in senha:
            criterios.append('V')
            break

    for numero in numeros:
        if numero in senha:
            criterios.append('V')
            break

    senha_valida = len(criterios) == 4

    return senha_valida

print(f'Senha válida: {validar_senha(senha)}')
