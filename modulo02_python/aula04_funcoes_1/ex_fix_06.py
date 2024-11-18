# EXERCÍCIOS DE FIXAÇÃO

# 6 - Função 'celsius_para_fahrenheit'
    # Crie uma função chamada 'celsius_para_fahrenheit' que receba um parâmetro celsius.
    # A função deve retornar a temperatura em Fahrenheit, calculada pela fórmula [fahrenheit = (celsius * 9/5) + 32].

    # Input:
        # celsius = 0

    # Resultado esperado:
        # 32.0

def celsius_para_fahrenheit(qnt_celsius: float):
    qnt_fahrenheit = (qnt_celsius * 9/5) + 32

    return qnt_fahrenheit

# Resolução 1:
celsius = 0
temperatura_fahrenheit = celsius_para_fahrenheit(celsius)
print(temperatura_fahrenheit)


# Resolução 2:
temperatura_fahrenheit2 = celsius_para_fahrenheit(0)
print(f'Temperatura em Fahrenheit: {temperatura_fahrenheit2:.2f}')
