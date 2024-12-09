# ATIVIDADE PRÁTICA 1

# Crie uma função que receba um nome e imprima uma saudação personalizada.

def saudacao(nome: str):
    saudacao_personalizada = f'\n{nome}, eu sei que você treme!'

    return saudacao_personalizada

print(saudacao(nome = input('Digite seu nome: ')))
