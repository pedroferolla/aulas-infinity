# Pratique e aprenda

# Objetivo: criar um programa que peça as 4 notas bimestrais e mostre a média.

# Instruções:
    # 1 - Solicitar as notas do usuário:
        # Use a função input() para pedir ao usuário que insira cada uma das quatro notas bimestrais.
        # Converta a entrada do usuário, de string para um número (float), para permitir cálculos.

    # 2 - Calcular a média das notas:
        # Some as quatro notas e divida o resultado por quatro, para obter a média.

    # 3 - Mostrar a média calculada para o usuário:
        # Use a função print() para exibir a média das notas calculada.

# Benefícios:
    # Fortalecer o entendimento de conceitos básicos e incentivar o pensamento lógico.
    # Promover a prática com a sintaxe de Python, desenvolvimento de programas interativos e aprimorar habilidades de depuração, preparando para conceitos avançados.

nota1 = float(input('Nota 1º bimestre: '))
nota2 = float(input('Nota 2º bimestre: '))
nota3 = float(input('Nota 3º bimestre: '))
nota4 = float(input('Nota 4º bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'Média: {media:.2f}')
