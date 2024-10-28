# EXERCÍCIOS DE FIXAÇÃO - PARTE 2/2

# 3 - Crie um dicionário onde as chaves sãos os nomes dos clientes e os valores são listas de compras realizadas 
    # (cada compra representada por uma string).
    # Implemente um código para contar o número total de compras feitas por cada cliente e exibir essas informações.

compras_clientes = {
    "Ana": ["leite", "pão", "maçã"],
    "Pedro": ["pão", "arroz", "leite", "maçã"],
    "Maria": ["maçã", "leite"]
}

for chave in compras_clientes:
    print(f'{chave}: {chave.__len__}')
    
