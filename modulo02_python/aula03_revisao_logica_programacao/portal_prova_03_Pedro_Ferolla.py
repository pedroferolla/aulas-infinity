# Prova PYIA - Revisão Geral

# Crie um dicionário para armazenar o nome e o preço de cinco produtos.
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço.
# À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor 
# associado a essa chave.
# Após a inserção de todos os produtos e preços, calcule o valor total da compra, somando todos os preços armazenados 
# no dicionário.
# Por fim, exiba o valor total da compra.

dicionario_produtos = {}
valor_total = 0


for i in range(5):
    dicionario_produtos[input('Produto: ')] = float(input('Preço: '))

for chave, valor in dicionario_produtos.items():
    print(f'Produto: {chave} - Preço: R$ {valor:.2f}')

for valor in dicionario_produtos.values():
    valor_total += valor

print(f'\nValor total da compra: R$ {valor_total:.2f}')
