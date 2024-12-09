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

def calcular_area_quadrado(lado: int):
    area_quadrado_calculada = lado * lado

    return area_quadrado_calculada

def calcular_area_circulo(raio: int):
    π = 3.14159265358979323846
    area_circulo_calculada = π * (raio * raio)

    return area_circulo_calculada

def calcular_area_retangulo(largura: int, altura: int):
    area_reangulo_calculada = largura * altura

    return area_reangulo_calculada

def calcular_area_triangulo(base: int, altura: int):
    area_triangulo_calculada = (base * altura) / 2

    return area_triangulo_calculada

def calcular_area_trapezio(base_maior: int, base_menor: int, altura: int):
    area_trapezio_calculada = [(base_maior + base_menor) * altura] / 2

    return area_trapezio_calculada
