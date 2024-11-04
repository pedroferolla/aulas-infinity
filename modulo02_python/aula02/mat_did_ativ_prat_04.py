# ATIVIDADE PRÁTICA 4

# Remova a fruta 'cereja' do conjunto 'frutas_vermelhas' e imprima o conjunto atualizado.

frutas_vermelhas = {'morango', 'cereja', 'framboesa'}

frutas_vermelhas.discard('cereja')

print(frutas_vermelhas)


# DISCARD retira um item do set, independentemente se ele estiver ou não presente, sem ocorrência de erro, caso não esteja.
# REMOVE retira um item do set, mas caso o item não esteja presente, há a incidência de erro.
