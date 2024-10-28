# Solicite ao usuário que insira dois números inteiros.
# Em seguida, use f-string para imprimir a soma desses números, por exemplo:

# Resultado esperado:
    # Digite o primeiro número: 10
    # Digite o segundo número: 5
    # -----------------------------
    # A soma de 10 e 5 é igual a 15.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
#soma = num1 + num2

mensagem = print(f'A soma de {num1} e {num2} é igual a {num1 + num2}')