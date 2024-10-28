# Objetivo: praticar a declaração e uso de variáveis de diferentes tipos, além de aprender a verificar e imprimir seus tipos em Python.

# Atividade 02: crie um programa que peça ao usuário para digitar:
    # 1. Seu nome;
    # 2. Sua idade;
    # 3. Sua altura;
    # 4. Em seguida, imprima esses valores e seus respectivos tipos.

# Observação: conhecer e utilizar diferentes tipos de variáveis é fundamental para manipular dados de maneira eficaz.

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

print(f'{nome} {type(nome)}')
print(f'{idade} {type(idade)}')
print(f'{altura} {type(altura)}')
