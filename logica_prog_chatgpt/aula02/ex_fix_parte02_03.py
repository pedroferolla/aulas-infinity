# EXERCÍCIOS DE FIXAÇÃO - PARTE2/2

# 3 - Escreva um programa que verifica se o usuário digitou corretamente um nome de usuário "admin" e senha "1234".
    # Se ele digitou, mostre "Login realizado com sucesso!".
    # Se não, mostre "Nome de usuário ou senha incorretos.".

usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

if usuario == 'admin' and senha == '1234':
    print('Login realizado com sucesso!')
else:
    print('Nome de usuário ou senha incorretos.')
