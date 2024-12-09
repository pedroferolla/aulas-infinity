# FUNÇÕES

# 6 - Contador de palavras:
    # Crie um programa que conte o número de palavras em uma frase e a frequência de cada palavra.

    # Objetivos:
        # - Defina uma função (contar_palavras), que receba uma frase e retorne o número total de palavras.
        # - Defina uma função (frequencia_palavras), que conte a frequência de cada palavras na frase.
        # - Crie uma função principal (analise_texto), que combine essas funções e exiba o resultado ao usuário.

    # Exemplo:
    # Digite uma frase: a casa é grande e a casa é bonita

    # Output esperado:
    # Número total de palavras: 9
    # Frequência das palavras:
    # a: 2
    # casa: 2
    # é: 2
    # grande: 1
    # e: 1
    # bonita: 1

# ERRO: enunciado original contém erro nos números do Output esperado e desconsidera a palavra 'e'.

def contar_palavras(frase: str):
    espacos_frase = 0
    for caractere in frase:
        if caractere == ' ':
            espacos_frase += 1

    palavras_contadas = espacos_frase + 1
    print(f'Número total de palavras: {palavras_contadas}')

def frequencia_palavras(frase: str):
    # Esta parte da função cria o split:
    lista = []
    nova_string = ''
    for caractere in frase:
        if caractere != ' ':
            nova_string += caractere
        else:
            lista.append(nova_string)
            nova_string = ''
    lista.append(nova_string)

    dicionario = {}
    for palavra in lista:
        if palavra in dicionario:
            dicionario[palavra] +=1
        else:    
            dicionario[palavra] = 1

    print('Frequência das palavras:')
    for chave, valor in dicionario.items():
        print(f'{chave}: {valor}')

def analise_texto():
    frase = input('Digite uma frase: ')

    contar_palavras(frase)
    frequencia_palavras(frase)  

analise_texto()


# GABARITO:
# def contar_palavras(frase):
    # return len(frase.split())

# def frequencia_palavras(frase):
    # palavras = frase.split()
    # frequencia = {}
    # for palavra in palavras:
        # if palavra in frequencia:
            # frequencia[palavra] += 1
        # else:
            # frequencia[palavra] = 1
    # return frequencia

# def analise_texto():
    # frase = input('Digite uma frase: ')
    # total_palavras = contar_palavras(frase)
    # frequencia = frequencia_palavras(frase)

    # print(f'Número total de palavras: {total_palavras}')
    # print('Frquência das palavras:')
    # for palavra, contagem in frequencia.items():
        # print(f'{palavra}: {contagem}')

# Exemplo de uso:
# analise_texto()
