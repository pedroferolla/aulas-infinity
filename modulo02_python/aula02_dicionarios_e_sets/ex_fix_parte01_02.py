# EXERCÍCIOS DE FIXAÇÃO - PARTE 1/2

# Dado o dicionário "contato" com as seguintes chaves e valores:
    # "telefone": "123456789"
    # "email": "contato@exemplo.com"

# Atualize o valor da chave "telefone" para "987654321".
# Imprima o dicionário após a atualização, mostrando as chaves e seus novos valores.

contato = {
    'telefone': '123456789',
    'email': 'contato@exemplo.com'
}

contato['telefone'] = '987654321'

print(contato)

for chave, valor in contato.items():
    print(f'{chave}: {valor}')
    