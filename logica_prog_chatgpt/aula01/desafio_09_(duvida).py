# Crie um programa que solicite ao usuário para digitar um número e depois imprima o tipo desse número (int ou float), por exemplo:

# Resultado esperado:
    # Digite um número: 10
    # --------------------
    # <class 'int'>

numero = (input('Digite um número: '))

print(type(numero))

# Como obter corretamente o tipo da variável, sendo que ela está declarada dentro de uma string?
# RESPOSTA: NÃO É PARA OBTER O TIPO DE VARIÁVEL A PARTIR DA ENTRADA DO USUÁRIO, MAS SIM, PREDEFINIR A CLASSE DE VARIÁVEL ANTES DE SOLICITAR.