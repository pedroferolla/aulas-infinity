# EXERCÍCIOS DE FIXAÇÃO

# 3 - Faça um programa que leia um nome de usuário e a sua senha, e não aceite a senha igual ao nome do usuário,
    # mostrando uma mensagem de erro e voltando a pedir as informações.

# RESULTADO ESPERADO:
    # Digite o nome de usuário: usuario123
    # Digite a senha: usuario123

    # ERRO: A senha não pode ser igual ao nome de usuário. Tente novamente.

    # Digite o nome de usuário: usuario123
    # Digite a senha: senha456

    # Cadastro realizado com sucesso!

usuario = input('Digite o nome de usuário: ')
senha = input('Digite a senha: ')

while usuario == senha:
    print('ERRO: A senha não pode ser igual ao nome de usuário. Tente novamente.')
    usuario = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')

print('Cadastro realizado com sucesso!')
