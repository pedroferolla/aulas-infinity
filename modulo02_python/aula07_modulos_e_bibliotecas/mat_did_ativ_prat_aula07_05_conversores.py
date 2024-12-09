# ATIVIDADE PRÁTICA 5

# Desenvolva um programa que permita ao usuário converter entre diferentes unidades de medida, como:
    # - Metros para pés
    # - Quilogramas para libras
    # - Celsius para Fahrenheit.

# Use módulos que contenham funções de conversão.

def converter_metros_para_pes(metros: float):
    return metros * 3.2808

def converter_quilogramas_para_libras(quilos: float):
    return quilos * 2.2046

def converter_celsius_para_fahrenheit(celsius: float):
    return (1.8 * celsius) + 32
