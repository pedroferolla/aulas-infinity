# ATIVIDADE PRÁTICA 8

# Crie uma função que aceite dois números e uma operação (por exemplo, adição, subtração, multiplicação e divisão) como 
# argumentos, e use funções lambda para realizar a operação especificada.
# A função deve retornar o resultado da operação.

def operacao_desejada(num1: int, operador: str, num2: int):

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado =  num1 * num2
    elif operador == '/':
        resultado = num1 / num2

    return resultado

print(operacao_desejada(5, '+', 8))
print(operacao_desejada(9, '-', 4))

# DÚVIDA: a função executa o que é solicitado, porém falta conseguir fazer através de função lambda.