# EXERCÍCIO DE FIXAÇÃO

# 2 - Funções Matemáticas em Módulos:
    # Crie um módulo chamado 'matematica.py', que deverá fazer as operações com 2 números, com as seguintes funções:
        # - somar()
        # - subtrair()
        # - multiplicar()
        # - dividir()
        # - fatorial_de_um_numero()

    # No arquivo 'principal.py', importe o módulo 'matematica' e use cada função com os números 10 e 5.
    # Mostre os resultados no console.

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
    divisao = x / y
    return divisao

def fatorial_de_um_numero(x: int):
    fatorial = 1
    
    while x > 1:
        fatorial *= x
        x -= 1
    return fatorial

# Teste da função fatorial_de_um_numero:
# print(fatorial_de_um_numero(4))
