# ATIVIDADE PRÁTICA

# Atividade 14:
    # Verificar status de taxa de desconto:
        # Crie um programa que peça ao usuário o preço original de um produto e a quantidade comprada.
        # Use if para verificar se a quantidade é maior que 10 para aplicar um desconto de 10% sobre o total.

preco_original = float(input('Digite o preço do produto: '))
quantidade = int(input('Digite a quantidade: '))

preco_desconto = preco_original * 0.9
preco_final_desconto = preco_desconto * quantidade

if quantidade > 10:
    print(f'Preço com desconto e valor total final: {preco_desconto} x {quantidade} = {preco_final_desconto}')
else:
    print(f'Preço normal e valor total final: {preco_original} x {quantidade} = {preco_original * quantidade}')
