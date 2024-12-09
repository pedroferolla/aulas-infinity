from aula_presencial_operacoes import aumentar_preco

macarrao = 5
frango = 20.1

# aumentar 10% em todos os preços
novo_preco_macarrao = aumentar_preco(macarrao, 10)
novo_preco_frango = aumentar_preco(frango, 10)

print(f'Novo preço frango: R$ {novo_preco_frango}')
print(f'Novo preço macarrão: R$ {novo_preco_macarrao}')


# Formas diferentes de importar:
import aula_presencial_operacoes
novo_preco_macarrao = aula_presencial_operacoes.aumentar_preco(macarrao, 10)
novo_preco_frango = aula_presencial_operacoes.aumentar_preco(frango, 10)


import aula_presencial_operacoes as op
novo_preco_macarrao = op.aumentar_preco(macarrao, 10)
novo_preco_frango = op.aumentar_preco(frango, 10)


from aula_presencial_operacoes import *
novo_preco_macarrao = aumentar_preco(macarrao, 10)
novo_preco_frango = aumentar_preco(frango, 10)
