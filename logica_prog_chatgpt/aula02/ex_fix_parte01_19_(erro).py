# EXERCÍCIOS DE FIXAÇÃO - PARTE1/2
# Operadores lógicos

# 19 - Solicite somente as horas atuais para o usuário e verifique se o horário atual é antes das 12:00 ou depois das 18:00.
    # Não utilize if.

# RESULTADO ESPERADO:
    # Digite o horário atual: 11
    # False <--------------------------- (ENUNCIADO PARECE CONTER ERRO)

horario = int(input('Digite o horário atual: '))

print(horario < 12 or horario > 18)


# COMENTÁRIO DO MONITOR EM SALA: independente do enunciado, é necessário buscar a solução de acordo com o gabarito fornecido.
    # Neste caso, deve-se criar um intervalo de variáveis