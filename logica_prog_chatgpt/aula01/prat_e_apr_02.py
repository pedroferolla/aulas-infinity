# Pratique e aprenda

# Objetivo:
    # Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    # Calcule o salário total e exiba o resultado (considere que você trabalha 20 dias no mês).

# Instruções:
    # 1 - Solicitar o salário mensal:
        # Use a função input() para pedir ao usuário que insira quanto ele ganha por mês.
        # Converta a entrada do usuário de string para um número (float), para permitir cálculos.

    # 2 - Solicitar o número de horas trabalhadas na semana:
        # Use a função input() para pedir ao usuário que insira o número de horas trabalhadas na semana.
        # Converta a entrada do usuário de string para um número (float), para permitir cálculos.

    # 3 - Calcular o total de horas trabalhadas no mês:
        # Multiplique o número de horas trabalhadas na semana por 4, para obter o total de horas trabalhadas no mês.

    # 4 - Calcular o salário por hora:
        # Divida o salário mensal pelo total de horas trabalhadas no mês, para obter o salário por hora.

    # 5 - Mostrar o salário por hora calculado para o usuário:
        # Use a função print() para exibir o salário por hora calculado.

salario_mes = float(input('Insira seu salário mensal: '))
horas_semana = float(input('Insira o número de horas trabalhadas na semana: '))

total_horas_mes = horas_semana * 4
salario_hora = salario_mes / total_horas_mes

print(f'Salário por hora: {salario_hora:.2f}')
