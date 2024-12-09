# EXERCÍCIO DE FIXAÇÃO

# 3 - Conversão de Unidades:
    # Crie um módulo chamado 'conversor.py', com funções para:
        # - Converter km para milhas
        # - Converter gramas para quilogramas
        # - Converter m/s para km/h
        # - Converter m³ em litros

    # No arquivo 'principal.py', importe o módulo 'conversor' e converta:
        # 10 km para milhas
        # 500 gramas para quilos
        # 10 m/s para km/h
        # 10 m³ para litros

def converter_km_para_milha(distancia_km: float):
    distancia_milhas = distancia_km * 0.621371
    return distancia_milhas

def converter_gramas_para_quilogramas(peso_gramas: float):
    peso_quilogramas = peso_gramas / 1000
    return peso_quilogramas

def converter_ms_para_kmh(velocidade_ms: float):
    velocidade_kmh = velocidade_ms * 3.6
    return velocidade_kmh

def converter_m3_para_litros(volume_metros_cubicos: float):
    volume_litros = volume_metros_cubicos * 1000
    return volume_litros
