senha = ''

while senha != '123':
    senha = input('Digite a senha: ')
    if senha == '123':
        print('Acesso liberado.')
    else:
        print('Senha incorreta.')
