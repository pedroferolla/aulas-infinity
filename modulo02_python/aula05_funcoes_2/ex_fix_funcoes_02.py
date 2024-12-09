# FUNÇÕES

# 2 - Cálculo de IMC:
    # Crie um programa que calcule o Índice de Massa Corporal (IMC) e classifique o resultado ('abaixo do peso', 
    # 'peso normal', 'sobrepeso' e 'obesidade').

    # Fórmula: IMC = peso (kg) / altura² (m)

    # a. Crie uma função ('calcular_imc'), que calcule o IMC com base no peso e altura, e retorne somente o valor do IMC.
    # b. Crie uma função ('classificar_imc'), que classifique o IMC conforme os critérios definidos:
        # Baixo peso: < 18.5
        # Peso normal: >= 18.5 e < 25
        # Excesso de peso: >= 25 e < 30
        # Obesidade: >= 30 e < 35
        # Obesidade extrema: >= 35
    # c. Crie uma função principal (imc_calculadora), que permita ao usuário inserir o peso e a altura, e exiba o IMC e sua 
       # classificação.

    # Input:
    # Digite seu peso (kg): 70
    # Digite sua altura (m): 1.75

    # Output esperado:
    # Seu IMC é 22.86
    # Classificação: Peso normal

def calcular_imc(peso: float, altura: float):
    imc_calculado = peso / (altura ** 2)
    return imc_calculado

def classificar_imc(imc: float):
    if imc < 18.5:
        return 'Baixo peso'
    elif imc >= 18.5 and imc < 25:
        return 'Peso normal'
    elif imc >= 25 and imc < 30:
        return 'Excesso de peso'
    elif imc >= 30 and imc < 35:
        return 'Obesidade'
    else:
        return 'Obesidade extrema'
    
def imc_calculadora():
    print('Calculadora de IMC')
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f'Seu IMC é {imc:.2f}')
    print(f'Classificação: {classificacao}')

imc_calculadora()
