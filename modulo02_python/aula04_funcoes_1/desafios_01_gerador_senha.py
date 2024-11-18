# DESAFIOS:

# 1 - Gerador de Senhas:
    # Crie uma função chamada 'gerar_senha', que gera uma senha aleatória com letras e números.
    # A função deve receber o comprimento desejado da senha.

    # Exemplo:
    # gerar_senha(12) pode retornar algo como 'a1B2c3D4e5F6'.

    # DICA: o código abaixo geraria uma vogal aleatória:
    # import random
    # caracteres = 'aeiou'
    # random.choice(caracteres)

    # Para gerar uma letra aleatória entre 'a', 'b', 'c' e 'd', o código seria o seguinte:
    # import random
    # caracteres = 'abcd'
    # random.choice(caracteres)

    # De que forma você poderia alterar esse código para colocar as letras e números?
    # Como você juntaria todos os caracteres da senha, se estamos gerando somente um caractere aleatório de cada vez?

import random

caracteres = '123456789abcdeiouABCD'

senha_tamanho = int(input('\nDigite o número de caracteres correspondente ao tamanho da senha: '))

def gerar_senha(senha_tamanho):
    senha = ''

    for i in range(senha_tamanho):
        caractere = random.choice(caracteres)
        senha += caractere

    return senha

print(f'Senha gerada aleatoriamente: {gerar_senha(senha_tamanho)}')
