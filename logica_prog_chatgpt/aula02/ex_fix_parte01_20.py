# EXERCÍCIOS DE FIXAÇÃO - PARTE1/2
# Operadores lógicos

# 19 - Verifique se um número é positivo ou está entre 20 e 30.

# RESULTADO ESPERADO:
    # Digite um número: 25
    # True

num = int(input('Digite um número: '))

positivo = num > 0
entre_20_e_30 = num >= 20 and num <=30

resultado = positivo or entre_20_e_30

print(resultado)
