# ATIVIDADE PRÁTICA 2

# Crie uma função que receba um horário e imprima "Bom dia", "Boa tarde" ou "Boa noite", conforme o horário.

def saudacao(horario: int):
    if horario >= 6 and horario < 12:
        mensagem = 'Bom dia!'
    elif horario >= 12 and horario < 18:
        mensagem = 'Boa tarde!'
    elif horario >= 18 and horario < 24 or horario >= 0 and horario < 6:
        mensagem = 'Boa noite!'
    else:
        mensagem = 'Horário inválido.'

    return mensagem

print(saudacao(54))
