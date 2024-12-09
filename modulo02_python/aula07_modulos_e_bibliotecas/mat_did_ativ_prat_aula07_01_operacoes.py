# ATIVIDADE PRÁTICA 1

# Crie um programa que será uma calculadora.
# Nesta calculadora, você deverá ter um módulo para as operações matemáticas.
# O arquivo principal deverá conter apenas um menu de escolha para o usuário (soma, subtração, multiplicação e divisão).

def somar(x: int, y: int):
    soma = x + y
    return soma

def subtrair(x: int, y: int):
    subtracao = x - y
    return subtracao

def multiplicar(x: int, y: int):
    multiplicacao = x * y
    return multiplicacao

def dividir(x: int, y: int):
    if y == 0:
        return 'Não é possível dividir por 0'
    divisao = x / y
    return divisao
