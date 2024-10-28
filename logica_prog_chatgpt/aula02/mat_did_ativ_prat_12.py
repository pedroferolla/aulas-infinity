# ATIVIDADE PRÁTICA

# Atividade 12:
    # Verificar classificação de IMC:
        # Crie um programa que calcule o Índice de Massa Corporal (IMC) e use if para classificar o resultado em:
            # - "Abaixo do peso"
            # - "Peso normal"
            # - "Sobrepeso"
            # - "Obesidade"

# Minhas observações:
    # A fórmula do IMC divide o peso do indivíduo pelo quadrado de sua altura.
    # Se alguém pesa 60kg e tem 1,7m de altura, por exemplo, o índice é calculado pela razão entre 60 e 2,89 (1,7 x 1,7), aproximadamente 20,76.

    # De acordo com os especialistas, indivíduos com índice entre 18,5 e 24,9 têm peso normal.
    # Uma pessoa está acima do peso quando seu IMC atinge 25.
    # E indivíduos com IMC a partir de 30 são classificados obesos.

    # São cinco faixas:
        # Menos de 18,5% - Abaixo do peso
        # 18,5% a 24,9% - Peso saudável
        # 25% a 29,9% - Sobrepeso
        # A partir de 30% - Obeso

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

resultado = peso / (altura * altura)

if resultado < 18.5:
    print('Abaixo do peso')
elif resultado < 25:
    print('Peso normal')
elif resultado < 30:
    print('Sobrepeso')
else:
    print('Obesidade')
