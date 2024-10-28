# ATIVIDADE PRÁTICA

# Atividade 03:
    # Verificação de maioridade e habilitação:
        # - Crie um programa que peça a idade do usuário e se ele possui habilitação (sim ou não).
        # - Use operadores lógicos para verificar se ele é maior de idade (>= 18) e possui habilitação.

idade = int(input('Digite sua idade: '))
habilitacao = input('Possui habilitação? (sim ou nao): ')

print(idade >= 18 and habilitacao == 'sim')
