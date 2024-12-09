# EXERCÍCIO DE FIXAÇÃO

# 1 - Saudações:
    # Crie um módulo chamado 'saudacoes.py', que receba um nome e mostre a mensagem:
        # 'Olá, {nome}! Bem-vindo!'

    # Em outro arquivo separado, chamado 'principal.py', importe o módulo 'saudacoes' e use a função 'diga_ola' para saudar 
    # três pessoas diferentes (por exemplo, 'Maria', 'João' e 'Ana')

from ex_fix_aula07_01_saudacoes import diga_ola, diga_ola_com_return

# Primeira forma de fazer:
diga_ola('Maria')
diga_ola('João')
diga_ola('Ana')

print('\n')

# Função com return (precisa do print):
print(diga_ola_com_return('Maria'))
print(diga_ola_com_return('João'))
print(diga_ola_com_return('Ana'))
