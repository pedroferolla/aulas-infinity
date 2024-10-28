# Prova - Revisão da Lógica da Programação

# Crie um programa em Python que simule um sistema de login.
# O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos.

# Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam.

# Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.

# Se todas as três tentativas falharem, o programa deve usar um loop for para exibir a mensagem de "Acesso bloqueado" 
# repetida três vezes.

usuario = input('\nDigite seu nome de usuário: ')
senha = input('Digite a senha: ')

tentativas = 3

while usuario != 'admin' and senha != '1234':
    tentativas -= 1
    print(f'\nUsuário ou senha incorreto. Restam {tentativas} tentativas.')

    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite a senha: ')

    if tentativas == 1:
        for i in range(0, 3):
            print('ACESSO BLOQUEADO!')
        break

else:
    print(f'\nBem-vindo {usuario}!')
