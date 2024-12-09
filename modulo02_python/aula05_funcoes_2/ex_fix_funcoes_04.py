# FUNÇÕES

# 4 - Conversor de temperatura:
    # Crie um programa que converta temperaturas entre Celsius e Fahrenheit, usando funções específicas para cada conversão.

    # Fórmulas:
    # °C > F°: (1.8 * °C) + 32
    # °F > °C: (°F - 32) / (5 / 9) 

    # Faça um menu de opções para o usuário poder escolher qual função ele quer executar.
        # 1 - Converter a temperatura de Celsius para Fahrenheit
        # 2 - Converter a temperatura de Fahrenheit para Celsius

    # Input:
    # Escolha uma opção:
    # [1] Converter Celsius para Fahrenheit
    # [2] Converter Fahrenheit para Celsius

    # Digite o número da opção desejada: 1

    # Digite a temperatura em Celsius: 25

    # Output esperado:
    # 25.0°C é igual a 77.0°F

def celsius_para_fahrenheit(temperatura_celsius: float):
    return (1.8 * temperatura_celsius) + 32

def fahrenheit_para_celsius(temperatura_fahrenheit: float):
    return (temperatura_fahrenheit - 32) / (5 / 9)

print('\nCONVERSOR DE TEMPERATURA')
while True:
    print('\nEscolha uma opção:\n[1] Converter Celsius para Fahrenheit\n[2] Converter Fahrenheit para Celsius')

    opcao = input('Digite o número da opção desejada: ')

    if opcao == '1':
        temperatura_celsius = float(input('\nDigite a temperatura em Celsius: '))
        print(f'{temperatura_celsius}°C é igual a {celsius_para_fahrenheit(temperatura_celsius):.1f}°F')
        break

    elif opcao == '2':
        temperatura_fahrenheit = float(input('\nDigite a temperatura em Fahrenheit: '))
        print(f'{temperatura_fahrenheit}°F é igual a {fahrenheit_para_celsius(temperatura_fahrenheit):.1f}°C')
        break

    else:
        print('\nOpção inválida.')
