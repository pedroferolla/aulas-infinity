# ATIVIDADE PRÁTICA

# Atividade 07:
    # Tabuada com Condicional:
        # Faça um programa que solicite um número ao usuário e use um laço While para exibir a tabuada desse número (de 1 a 10),
        # mas apenas para os resultados que forem múltiplos de 3.

numero = int(input('Digite um número: '))
fator = 1

while fator <= 10:
    tabuada = numero * fator
    if tabuada % 3 == 0:
        print(f'{numero} x {fator} = {tabuada}')
    fator += 1
        


# DÚVIDA: VERIFICAR SE A QUESTÃO FOI CORRETAMENTE ENTENDIDA E SE O LOOP ESTÁ CORRETO.
        # PERGUNTAR POR QUE O 'ELSE' ACARRETA EM LOOP INFINITO.


