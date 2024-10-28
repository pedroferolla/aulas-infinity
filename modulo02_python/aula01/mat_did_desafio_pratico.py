# DESAFIO PRÁTICO

# Suponha que você está gerenciando uma competição esportiva e tem uma lista de tuplas representando os resultados das 
# equipes, em diferentes modalidades.
# Cada tupla contém o nome da equipe, seguido por uma lista de pontuações obtidas em cada rodada da competição.

    # 1 - Calcule a média das pontuações de cada equipe e armazene esses valores em uma nova lista chamada "medias".
    # 2 - Ordene a lista "medias" em ordem decrescente.
    # 3 - Crie uma nova lista chamada "classificacao", que contém tuplas, onde cada tupla contém o nome da equipe e sua 
        # média de pontuações.
    # 4 - Exiba na tela a classificação final das equipes, mostrando o nome da equipe e sua média, da equipe com a 
        # pontuação mais alta para a mais baixa.

# print(f'{media_equipe1:.2f}')

lista = [
    ('River Plate', 8.6, 6.4, 4.4),
    ('GALO', 8.1, 7.3, 9.4),
    ('Peñarol', 7.6, 6.0, 1.9),
    ('Bostafogo', 7.1, 6.8, 6.9)
]

media_equipe1 = (lista[0][1] + lista[0][2] + lista[0][3]) / 3
media_equipe2 = (lista[1][1] + lista[1][2] + lista[1][3]) / 3
media_equipe3 = (lista[2][1] + lista[2][2] + lista[2][3]) / 3
media_equipe4 = (lista[3][1] + lista[3][2] + lista[3][3]) / 3

medias = [media_equipe1, media_equipe2, media_equipe3, media_equipe4]
medias = sorted(medias, reverse = True)

classificacao = [
    (lista[1][0], media_equipe2),
    (lista[3][0], media_equipe4),
    (lista[0][0], media_equipe1),
    (lista[2][0], media_equipe3)
]

print(classificacao)

# colocacao = 1

# for equipe in classificacao:
#     print(f'{colocacao}º lugar: {classificacao[0][0]} - Média de pontos: {classificacao[0][1]}')
#     colocacao += 1
#     classificacao += 1
