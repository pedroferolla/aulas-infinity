def somar_numeros(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    
    return soma

soma_1 = somar_numeros(2, 4, 6)

print(soma_1)                # | Print que chama a função pela variável de resultado
print(somar_numeros(3, 5))   # | Print que chama a função diretamente, atribuindo os argumentos.
