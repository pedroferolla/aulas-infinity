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

from ex_fix_aula07_03_conversor import *

print(f'10 km para milhas: {converter_km_para_milha(10)} milhas')
print(f'500 gramas para quilos: {converter_gramas_para_quilogramas(500)} kgs')
print(f'10 m/s para km/h: {converter_ms_para_kmh(10)} km/h')
print(f'10 m³ para litros: {converter_m3_para_litros(10)} litros')
