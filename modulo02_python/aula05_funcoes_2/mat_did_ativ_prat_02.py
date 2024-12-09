# ATIVIDADE PRÁTICA 2

# Crie um programa que define uma função 'calcular_area_retangulo', que recebe doi argumentos, comprimento e largura de um 
# retângulo, e retorna a área desse retângulo.
# Em seguida, o programa deve solicitar ao usuário que insira o comprimento e a largura, e imprimir a área calculada.

def calcular_area_retangulo(comprimento: float, largura: float):
    area_retangulo = comprimento * largura

    return area_retangulo

print('Área calculada:', calcular_area_retangulo(comprimento= int(input('Comprimento: ')), largura= int(input('Largura: '))), 'm²')
