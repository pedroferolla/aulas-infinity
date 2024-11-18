def somar(numero_1: float, numero_2: float):
    somatorio = numero_1 + numero_2
    return somatorio

# Função lambda:
somar_nova = lambda x, y: x + y


def somar_3_numeros(numero_1: float, numero_2: float, numero_3: float):
    somatorio = numero_1 + numero_2 + numero_3
    return somatorio

# Função lambda:
soma_3 = lambda num_1, num_2, num_3: num_1 + num_2 + num_3


resultado_1 = somar(13 ,4)

resultado_2 = somar_nova(8, 2)

resultado_3 = soma_3(10, 9, 3)

print(resultado_1)
print(resultado_2)
print(resultado_3)

