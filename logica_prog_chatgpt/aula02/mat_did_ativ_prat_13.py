# ATIVIDADE PRÁTICA

# Atividade 13:
    # Sistema de login simples:
        # Desenvolva um programa que peça ao usuário um nome de usuário e uma senha.
        # Use if para verificar se são iguais a "admin" e "1234", respectivamente.

usuario = input('Nome de usuário: ')
senha = input('Senha: ')

if usuario == 'admin' and senha == '1234':
    print('Acesso liberado')
else:
    print('Acesso negado')
