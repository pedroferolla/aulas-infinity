# Faça um programa que peça ao usuário para digitar dois números e imprima o tipo de cada um desses números.

# Resultado esperado:
    # Digite o primeiro número: 10
    # Digite o segundo número: 5.5
    # ----------------------------
    # <class 'int'>
    # <class 'float'>

n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')

print(type(n1))
print(type(n2))

# Como obter corretamente o tipo da variável, sendo que ela está declarada dentro de uma string?