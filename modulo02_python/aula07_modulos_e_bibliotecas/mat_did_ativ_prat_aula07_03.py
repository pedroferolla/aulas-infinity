# ATIVIDADE PRÁTICA 3

# Crie um programa que permite ao usuário calcular a área e o perímetro de formas geométricas simples, como quadrados, 
# retângulos, e círculos.
# Use funções matemáticas do módulo 'math' para realizar os cálculos.

import math

def calcular_area_quadrado(lado: int):
    area_quadrado_calculada = math.pow(lado, 2)
    return area_quadrado_calculada

def calcular_perimetro_quadrado(lado: int):
    perimetro_quadrado_calculado = lado * 4
    return perimetro_quadrado_calculado


def calcular_area_retangulo(largura: int, altura: int):
    area_retangulo_calculada = largura * altura
    return area_retangulo_calculada

def calcular_perimetro_retangulo(largura: int, altura: int):
    perimetro_retangulo_calculado = (largura * 2) + (altura * 2)
    return perimetro_retangulo_calculado


def calcular_area_circulo(raio: int):
    area_circulo_calculada = math.pi * math.pow(raio, 2)
    return area_circulo_calculada

def calcular_perimetro_circulo(raio: int):
    perimetro_circulo_calculado = 2 * math.pi * raio
    return perimetro_circulo_calculado


print('\nCALCULADORA DE ÁREA E PERÍMETRO')

while True:
    print('\nMenu:')
    print('[1] Quadrado')
    print('[2] Retângulo')
    print('[3] Círculo')
    print('[4] Encerrar programa.')

    escolha_usuario = input('\nDigite o índice desejado: ')

    if escolha_usuario == '1':
        while True:
            print('\n[1] Área de um quadrado.')
            print('[2] Perímetro de um quadrado.')
            print('[3] Voltar')

            operacao_usuario = input('\nDigite o índice da operação desejada: ')

            if operacao_usuario == '1':
                lado = int(input('Comprimento do lado do quadrado: '))
                print(f'Área do quadrado: {calcular_area_quadrado(lado)}')
            elif operacao_usuario == '2':
                lado = int(input('Comprimento do lado do quadrado: '))
                print(f'Perímetro do quadrado: {calcular_perimetro_quadrado(lado)}')
            elif operacao_usuario == '3':
                break
            else:
                print('Opção inválida.')

    elif escolha_usuario == '2':
        while True:
            print('\n[1] Área de um retângulo.')
            print('[2] Perímetro de um retângulo.')
            print('[3] Voltar')

            operacao_usuario = input('\nDigite o índice da operação desejada: ')

            if operacao_usuario == '1':
                largura = int(input('Comprimento da largura do retângulo: '))
                altura = int(input('Comprimento da altura do retângulo: '))
                print(f'Área do retângulo: {calcular_area_retangulo(largura, altura)}')
            elif operacao_usuario == '2':
                largura = int(input('Comprimento da largura do retângulo: '))
                altura = int(input('Comprimento da altura do retângulo: '))
                print(f'Perímetro do retângulo: {calcular_perimetro_retangulo(largura, altura)}')
            elif operacao_usuario == '3':
                break
            else:
                print('Opção inválida.')

    elif escolha_usuario == '3':
        while True:
            print('\n[1] Área de um círculo.')
            print('[2] Perímetro de um círculo.')
            print('[3] Voltar')

            operacao_usuario = input('\nDigite o índice da operação desejada: ')

            if operacao_usuario == '1':
                raio = int(input('Comprimento do raio do círculo: '))
                print(f'Área do círculo: {calcular_area_circulo(raio):.2f}')
            elif operacao_usuario == '2':
                raio = int(input('Comprimento do raio do círculo: '))
                print(f'Perímetro do círculo: {calcular_perimetro_circulo(raio):.2f}')
            elif operacao_usuario == '3':
                break
            else:
                print('Opção inválida.')

    elif escolha_usuario == '4':
        print('Programa encerrado')
        break

    else:
        print('Opção inválida.')
