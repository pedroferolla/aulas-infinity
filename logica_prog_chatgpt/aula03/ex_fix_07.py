# EXERCÍCIOS DE FIXAÇÃO

# 7 - Implemente um programa que solicite ao usuário que digite um nome de usuário e uma senha.
    # O programa só deve permitir o acesso quando o usuário digitar corretamente um nome de usuário e senha predefinidos.
    # Caso contrário, deve continuar solicitando até que o usuário entre com as informações corretas.

# RESULTADO ESPERADO:
    # Digite o nome de usuário: admin
    # Digite a senha: 12345
    # Nome de usuário ou senha incorretos. Tente novamente.

    # Digite o nome de usuário: admin
    # Digite a senha: admin
    # Nome de usuário ou senha incorretos. Tente novamente.

    # Digite o nome de usuário: admin
    # Digite a senha: 123
    # Acesso concedido.

usuario = input('Digite o nome de usuário: ')
senha = input('Digite a senha: ')

while usuario != 'admin' or senha != '123':
    print('Nome de usuário ou senha incorretos. Tente novamente.')
    usuario = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')

print('Acesso concedido.')
