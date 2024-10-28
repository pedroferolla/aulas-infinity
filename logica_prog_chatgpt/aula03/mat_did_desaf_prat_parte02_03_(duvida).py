# DESAFIOS PRÁTICOS

# Instruções:
    # 3 - Soma de dígitos:
        # Escreva um programa que solicite um número ao usuário e use um laço While para somar os dígitos do número até que
        # a soma seja um único dígito.

# Benefícios: praticar o uso de operadores aritméticos em Python e entender como realizar cálculos matemáticos
            # básicos com variáveis.



# DÚVIDA: COMO DESMEMBRAR OS CARACTERES DE UMA VARIÁVEL INT?

# OBSERVAÇÃO: É POSSÍVEL DESMEMBRAR OS CARACTERES VIA DIVISÃO INTEIRA, MAS ISSO FICA LIMITADO AO PRÉ ESTABELECIMENTO
            # DE CASA DECIMAIS MÁXIMAS, PELO PROGRAMADOR (UNIDADES, DEZENAS, CENTENAS, MILHARES, ETC).
            # COMO CRIAR UM MODO EM QUE O PRÓPRIO SISTEMA CONSIGA FAZER O FRACIONAMENTO, INDEPENDENTE DO TAMANHO
            # DO NÚMERO INSERIDO PELO USUÁRIO?

num = 123
# num = int(input('Digite um número inteiro para somar seus caracteres: '))

centenas = num // 100
num = num % 100

dezenas = num // 10
num = num % 10

unidades = num

casa_decimal = centenas + dezenas + unidades

casa_dezena = casa_decimal // 10
casa_decimal % 10

casa_unidade = casa_decimal

soma = casa_dezena + casa_unidade

while casa_decimal > 1:
    num 