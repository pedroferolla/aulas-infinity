# EXERCÍCIOS DE APRENDIZAGEM

# 3 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
    # As perguntas são:
        # a. "Telefonou para a vítima?"
        # b. "Esteve no local do crime?"
        # c. "Mora perto da vítima?"
        # d. "Devia para a vítima?"
        # e. "Já trabalhou com a vítima?"

    # O programa deve, no final, emitir uma classificação sobre a participação da pessoa no crime.
    # Se a pessoa responder "sim" a duas questões, ela deve ser classificada como "Suspeita".
    # Se a pessoa responder "sim" entre três e quatro questões, como "Cúmplice".
    # Se a pessoa responder "sim" a cinco questões, como "Assassino(a)".
    # Caso contrário, ela será classificada como "Inocente".

# Minha tentativa:
# p1 = input('Telefonou para a vítima? (sim ou não): ')
# p2 = input('Esteve no local do crime? (sim ou não): ')
# p3 = input('Mora perto da vítima? (sim ou não): ')
# p4 = input('Devia para a vítima? (sim ou não): ')
# p5 = input('Já trabalhou com a vítima? (sim ou não): ')

# sim = 1
# não = 0 <------------- COMO CONVERTER UMA RESPOSTA (ENTRADA DO USUÁRIO STRING) EM FORMATO INT, PARA QUE POSSA SER CONTADO POSTERIOMENTE?

# if p1 + p2 + p3 + p4 + p5 <= 1:
#     print('Inocente')
# elif p1 + p2 + p3 + p4 + p5 == 2:
#     print('Suspeito(a)')
# elif p1 + p2 + p3 + p4 + p5 <= 4:
#     print('Cúmplice')
# else:
#     print('Assassino(a)')



# GABARITO:
# Inicializa o contador de respostas afirmativas:
contador_sim = 0

# Faz as cinco perguntas:
print("Responda com 'sim' ou 'não' para as seguintes perguntas: ")

resposta = input('1. Telefonou para a vítima? ').lower()
if resposta == 'sim':
    contador_sim += 1

resposta = input('2. Esteve no local do crime? ').lower()
if resposta == 'sim':
    contador_sim += 1

resposta = input('3. Mora perto da vítima? ').lower()
if resposta == 'sim':
    contador_sim += 1

resposta = input('4. Devia para a vítima? ').lower()
if resposta == 'sim':
    contador_sim += 1

resposta = input('5. Já trabalhou com a vítima? ').lower()
if resposta == 'sim':
    contador_sim += 1

# Determina a classificação com base no número de respostas afirmativas:
if contador_sim == 2:
    print('Classificação: Suspeito(a)')
elif contador_sim == 3 or contador_sim == 4:
    print('Classificação: Cúmplice')
elif contador_sim == 5:
    print('Classificação: Assassino(a)')
else:
    print('Classificação: Inocente')
