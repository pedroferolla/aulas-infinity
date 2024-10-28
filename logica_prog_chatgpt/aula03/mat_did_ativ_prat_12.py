# ATIVIDADE PRÁTICA

# Atividade 11:
    # Senha correta:
        # Desenvolva um programa que peça ao usuário para digitar um senha.
        # Continue pedindo até que a senha correta (previamente definida) seja inserida.

senha = 'GALO'
tentativa = ''

while tentativa != 'GALO':
    tentativa = input('Digite a senha: ')
    if tentativa == senha:
        print('Acesso liberado.')
    else:
        print('Senha incorreta. Tente novamente.')


# OBS: EXISTE UM EXEMPLO IDÊNTICO À QUESTÃO, NO PRÓPRIO MATERIAL DIDÁTICO.

# LEMBRAR QUE É NECESSÁRIO COLOCAR A VARIÁVEL DENTRO DO WHILE, PARA QUE DEPENDA DE UMA ÚNICA AÇÃO DO USUÁRIO.
# CASO CONTRÁRIO, O LOOP APENAS IMPRIME A MENSAGEM INFINITAMENTE.
