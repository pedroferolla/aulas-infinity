# Solicite ao usuário que insira o ano de nascimento.
# Calcule a idade usando f-string, por exemplo:

# Resultado esperado:
    # Digite o ano de nascimento: 1990
    # --------------------------------
    # Em 2024, você tem 34 anos de idade.

nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = 2024

print(f'Em {ano_atual}, você tem {ano_atual - nascimento} anos de idade.')