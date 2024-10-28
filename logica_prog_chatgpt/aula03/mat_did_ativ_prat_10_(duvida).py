# ATIVIDADE PRÁTICA

# Atividade 10:
    # Soma até 50:
        # Escreva um programa que use um laço While para somar números consecutivos, começando de 1
        # e termine quando a soma atingir ou ultrapassar 50.

soma = 0    # <-------------- COMO INICIAR A SOMA ATRAVÉS DO PRIMEIRO RESULTADO (1 + 2 = 3)?
num = 1
# proximo = num + 1

# while soma <= 50:
#     soma = soma + num
#     num = num + 1
#     print(f'Soma = {soma}')
    
#     if soma > 50:
#         break

while soma <= 50:
    soma += num
    num += 1
    
    print(soma)
    
    if soma > 50:
        break
    