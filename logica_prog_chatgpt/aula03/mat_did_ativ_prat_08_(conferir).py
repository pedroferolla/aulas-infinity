# ATIVIDADE PRÁTICA

# Atividade 08:
    # Média de notas:
        # Desenvolva um programa que solicite as notas dos alunos até que o usuário digite -1.
        # Calcule e exiba a média das notas inseridas.

nota = float(input('Digite a primeira nota: '))
proxima = float()
divisor = 1


while proxima >= 0:
    proxima = float(input('Digite a próxima nota: '))
    if proxima >= 0:
        nota += proxima
        divisor += 1
        media = float(nota / divisor)
        
print(f'Média = {media:.2f}')


# DÚVIDA: COMO CALCULAR O DIVISOR (NÚMERO DE NOTAS INSERIDAS) PARA QUE SE DIVIDA PELA SOMATÓRIA DAS NOTAS E SE OBTER A MÉDIA?
        # POR QUE A MÉDIA ESTÁ SENDO CALCULADA COMO INT AO INVÉS DE FLOAT?

# OBS: APARENTEMENTE O PROGRAMA ESTÁ RODANDO CORRETAMENTE, MAS CONFERIR SE A QUESTÃO FOI COMPREENDIDA DA MANEIRA CERTA.
