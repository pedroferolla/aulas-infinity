# EXERCÍCIOS DE FIXAÇÃO

# 2 - Ajustando Temperaturas
    # Você tem uma lista de temperaturas em Fahrenheit e deseja convertê-las para Celsius.
    # Use a função 'map' para realizar a conversão.

temperaturas_fahrenheit = [100, 128, 74, 16]

temp_convertidas_para_celsius = list(map(lambda temperatura: round((temperatura - 32) / 1.8, 1), temperaturas_fahrenheit))

print(temp_convertidas_para_celsius)
