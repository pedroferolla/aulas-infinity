# Faça um programa que solicite ao usuário para digitar o seu ano de nascimento e calcule a idade do usuário.

# Resultado esperado:
    # Digite o ano de seu nascimento: 1990
    # ------------------------------------
    # Em 2024, você tem 34 anos de idade.

ano_nascimento = int(input('Digite o ano de seu nascimento: '))
ano_atual = 2024

print(f'Em {ano_atual}, você tem {ano_atual - ano_nascimento} anos de idade.')
