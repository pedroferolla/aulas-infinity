# EXERCÍCIOS DE APRENDIZAGEM

# 5 - Faça um programa que recebe o salário de um colaborador.
    # Calcule o reajuste segundo o seguinte critério, baseado no salário atual do colaborador:

    # Até R$ 280,00: reajuste de 20%
    # Entre R$ 280,01 e R$ 700,00: reajuste de 15%
    # Entre R$ 700,01 e R$ 1.500,00: reajuste de 10%
    # Maior que R$ 1.500,00: reajuste de 5%

    # Após o aumento ser calculado, informe na tela:
        # a. O salário antes do reajuste;
        # b. O percentual de aumento aplicado;
        # c. O valor do aumento;
        # d. O novo salário, após o aumento.

salario = float(input('Insira seu salário: '))
print(f'- Salário antes do reajuste: {salario}')

if salario <= 280:
    print('- O percentual de aumento aplicado é: 20%')
elif salario <= 700:
    print('- O percentual de aumento aplicado é: 15%')
elif salario <= 1500:
    print('- O percentual de aumento aplicado é: 10%')
else:
    print('- O percentual de aumento aplicado é: 5%')

if salario <= 280:
    print(f'- O valor de aumento é: R$ {salario * 0.2}')
elif salario <= 700:
    print(f'- O valor de aumento é: R$ {salario * 0.15}')
elif salario <= 1500:
    print(f'- O valor de aumento é: R$ {salario * 0.1}')
else:
    print(f'- O valor de aumento é: R$ {salario * 0.05}')

if salario <= 280:
    print(f'- O novo salário, após o aumento é: R$ {(salario * 0.2) + (salario)}')
elif salario <= 700:
    print(f'- O novo salário, após o aumento é: R$ {(salario * 0.15) + (salario)}')
elif salario <= 1500:
    print(f'- O novo salário, após o aumento é: R$ {(salario * 0.1) + (salario)}')
else:
    print(f'- O novo salário, após o aumento é: R$ {(salario * 0.05) + (salario)}')


# GABARITO:
# salario_atual = float(input('Digite o salário atual do colaborador: R$ '))

# Determina o percentual de aumento e calcula o novo salário baseado nas faixas de salário:
# if salario_atual <= 280.00:
    # percentual_aumento = 20
# elif salario_atual <= 700.00:
    # percentual_aumento = 15
# elif salario_atual <= 1500.00:
    # percentual_aumento = 10
# else:
    # percentual_aumento = 5

# Calcula o valor do aumento e o novo salário:
# valor_aumento = salario_atual * percentual_aumento / 100
# novo_salario = salario_atual + valor_aumento

# Imprime os resultados:
# print(f'Salário antes do reajuste: R$ {salario_atual:.2f}')
# print(f'Percentual de aumento aplicado: {percentual_aumento}%')
# print(f'Valor do aumento: R$ {valor_aumento:.2f}')
# print(f'Novo salário após o aumento: R$ {novo_salario:.2f}')
