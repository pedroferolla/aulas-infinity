# EXERCÍCIO DE FIXAÇÃO

# 5 - Módulo de Cálculos Geométricos:
    # Crie um módulo chamado 'geometria.py', com as seguintes funções:
        # - Calcular a área do quadrado
        # - Calcular a área do círculo
        # - Calcular a área do retângulo
        # - Calcular a área do triângulo
        # - Calcular a área do trapézio

    # No arquivo 'principal.py', importe o módulo 'geometria' e calcule:
        # - A área de um quadrado com lado de 4 unidades
        # - A área de um retângulo com largura 5 e altura 10 unidades
        # - A área de um círculo com raio 3 unidades

    # Imprima os resultado no console.

from ex_fix_aula07_05_geometria import *

print(f'A área de um quadrado com lado de 4 unidades: {calcular_area_quadrado(4)}')

print(f'A área de um retângulo com largura 5 e altura 10 unidades: {calcular_area_retangulo(5, 10)}')

print(f'A área de um círculo com raio 3 unidades: {calcular_area_circulo(3)}')
