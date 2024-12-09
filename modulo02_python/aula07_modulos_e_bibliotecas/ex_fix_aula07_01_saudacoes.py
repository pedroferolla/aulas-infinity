# EXERCÍCIO DE FIXAÇÃO

# 1 - Saudações:
    # Crie um módulo chamado 'saudacoes.py', que receba um nome e mostre a mensagem:
        # 'Olá, {nome}! Bem-vindo!'

    # Em outro arquivo separado, chamado 'principal.py', importe o módulo 'saudacoes' e use a função 'diga_ola' para saudar 
    # três pessoas diferentes (por exemplo, 'Maria', 'João' e 'Ana')

def diga_ola(nome: str):
    print(f'Olá, {nome}! Bem-vindo!')

def diga_ola_com_return(nome: str):
    return f'Olá, {nome}! Bem-vindo!'
