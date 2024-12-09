# ATIVIDADE PRÁTICA 1

# Crie um programa que solicita ao usuário que insira três notas e, em seguinda, calcule a média dessas três notas usando 
# uma função.
# A função deve receber as três notas como argumentos e retornar a média.
# Por fim, o programa deve imprimir a média calculada.

def calcular_media(nota1: float, nota2: float, nota3: float):
    media = (nota1 + nota2 + nota3) / 3

    return media

print('Média:', calcular_media(nota1 = int(input('1ª nota: ')), nota2 = int(input('2º nota: ')), nota3 = int(input('3ª nota: '))))
