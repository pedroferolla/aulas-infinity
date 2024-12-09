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

from ex_fix_aula07_02_matematica import somar, dividir, multiplicar, subtrair, fatorial_de_um_numero

print(f'Soma de 10 e 5: {somar(10, 5)}')
print(f'Subtração de 10 e 5: {dividir(10, 5)}')
print(f'Multiplicação de 10 e 5: {multiplicar(10, 5)}')
print(f'Divisão de 10 e 5: {dividir(10, 5)}')
print(f'Fatorial de 5: {fatorial_de_um_numero(5)}')
