# DESAFIOS:
# URNA ELETRÔNICA:

# Você deve criar um sistema de votação em Python que permita registrar votos para diferentes candidatos e 
# exibir o total de votos para cada candidato.

# 1 - Criação do Dicionário de Candidatos:
    # Crie um dicionário chamado "candidatos" onde as chaves são os nomes dos candidatos e os valores são outros 
    # dicionários que contêm uma chave "votos" com o valor inicial igual a 0.

# (Baixar arquivo inicial)

    # Exemplo:
    # candidatos = {
    #     "A": {"votos": 0},
    #     "B": {"votos": 0},
    #     "C": {"votos": 0},
    #     }

# 2 - Mostrar a lista de candidatos:
    # Escreva um código que exiba a lista de candidatos disponíveis.
    # Cada nome de candidato deve ser impresso em uma nova linha.

    # Exemplo:
    # Candidatos disponíveis:
    # Candidato A
    # Candidato B
    # Candidato C

# 3 - Registrar um voto:
    # Solicite ao usuário que digite o nome do candidato em quem ele deseja votar e adicione 1 voto para esse candidato.

    # Exemplo:
    # Digite o nome do candidato em quem você deseja votar (ou 'sair' para encerrar): B
    # Voto registrado para o candidato B.

# 4 - Repetir votação:
    # Adicione uma parte no código, na pergunta do nome do candidato, se a resposta for 'sair', finalize a votação.
    # Se for o nome do candidato, repita a pergunta.

    # Exemplo:
    # Digite o nome do candidato em quem você deseja votar (ou 'sair' para encerrar): B
    # Voto registrado para o candidato B.
    # Digite o nome do candidato em quem você deseja votar (ou 'sair' para encerrar): A
    # Voto registrado para o candidato A.
    # Digite o nome do candidato em quem você deseja votar (ou 'sair' para encerrar): B
    # Voto registrado para o candidato B.
    # Digite o nome do candidato em quem você deseja votar (ou 'sair' para encerrar): sair
    # Votação encerrada.

# 5 - Exibir resultado:
    # Quando o usuário digitar 'sair', exiba o total de votos para cada candidato.

    # Exemplo:
    # Digite o nome do candidato em quem você deseja votar (ou 'sair' para encerrar): sair
    # Votação encerrada.

    # Resultado dos votos:
    # Candidato A - Votos: 1
    # Candidato B - Votos: 2
    # Candidato C - Votos: 0

# 6 - Identificar o Vencedor:
    # Após o término da votação, determine qual candidato recebeu o maior número de votos e informe quem foi 
    # o vencedor.

    # Exemplo:
    # Resultado dos votos:
    # Candidato A - Votos: 1
    # Candidato B - Votos: 2
    # Candidato C - Votos: 0

    # Vencedor da eleição: Candidato B

# 7 - Calcule a porcentagem de votos que cada candidato recebeu em relação ao total de votos e exiba esses valores.

    # Exemplo:
    # Resultado dos votos:
    # Resultado dos votos:
    # Candidato A - Votos: 1 - Percentual: 33.3%
    # Candidato B - Votos: 2 - Percentual: 66.3%
    # Candidato C - Votos: 0 - Percentual: 0%

    # Vencedor da eleição: Candidato B

# 8 - Validar candidato:
    # Valide se o candidato que o usuário votou existe. Se não existir, retorne uma mensagem de erro e pergunte 
    # novamente qual é o candidato que ele deseja votar.

candidatos = {
    "A": {"votos": 0},
    "B": {"votos": 0},
    "C": {"votos": 0},
    }

print('Candidatos disponíveis:')

for i in candidatos:
    print(f'Candidato {i}')

voto_a = 0
voto_b = 0
voto_c = 0

while True:

    voto_eleitor = input('\nDigite o nome do candidato em quem você deseja votar (ou "sair" para encerrar): ')

    if voto_eleitor == 'sair':
        print('\nVotação encerrada.')
        break
    elif voto_eleitor == 'A':
        voto_a += 1
        candidatos['A'] = {'votos': voto_a}
        print('Voto registrado para o candidato A')
    elif voto_eleitor == 'B':
        voto_b += 1
        candidatos['B'] = {'votos': voto_b}
        print('Voto registrado para o candidato B')
    elif voto_eleitor == 'C':
        voto_c += 1
        candidatos['C'] = {'votos': voto_c}
        print('Voto registrado para o candidato C')
    else:
        print('Candidato não encontrado. Por favor, verifique o nome e tente novamente.')

votos_total = voto_a + voto_b + voto_c

print(f'\nResultado dos votos:')
for chave, valor in candidatos.items():
    print(f"Candidato {chave} - Votos: {valor['votos']} - Percentual: {(valor['votos'] / votos_total) * 100 :.1f}%")

if voto_a > voto_b and voto_a > voto_c:
    print('\nVencedor da eleição: Candidato A')
elif voto_b > voto_a and voto_b > voto_c:
    print('\nVencedor da eleição: Candidato B')
elif voto_c > voto_a and voto_c > voto_b:
    print('\nVencedor da eleição: Candidato C')
