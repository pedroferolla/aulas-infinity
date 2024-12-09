# Prova PYIA - Função 2

# Crie uma função chamada 'maior_numero', que receberá três números como argumentos.
# Esta função deve comparar os três números e identificar qual deles é o maior.
# Para isso, utilize uma estrutura de controle, que verifique qual número é maior que os outros dois.
# A função deve então retornar o maior número encontrado.

def maior_numero(x: int, y: int, z:int):
    if x > y and x > z:
        maior_identificado = x
    elif y > x and y > z:
        maior_identificado = y
    elif z > x and z > y:
        maior_identificado = z

    return maior_identificado

print(maior_numero(x = 4, y = 8, z = 2))
