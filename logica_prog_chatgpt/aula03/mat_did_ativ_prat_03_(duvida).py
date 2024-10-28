# ATIVIDADE PRÁTICA

# Atividade 03:
    # Tabuada de um número:
        # Faça um programa que solicite um número ao usuário e use um laço While para exibir a tabuada dese número (de 1 a 10).

numero = int(input('Digite um número: '))
fator = 1
# resultado = numero * fator    <-------------------- DÚVIDA!

while fator <= 10:
    print(f'{numero} x {fator} = {numero * fator}')
    fator += 1

# DÚVIDA: POR QUE NÃO É POSSÍVEL USAR A VARIÁVEL 'RESULTADO' NA F-STRING, NO LUGAR DE '{numero * fator}'?
