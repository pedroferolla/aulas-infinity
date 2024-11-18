# EXERCÍCIOS DE FIXAÇÃO - PARTE 2/2

# 5 - Crie um dicionário para armazenar um cadastro de contatos.
    # Cada contato deve ter um nome como chave e um número de telefone como valor.
    # Pergunte se o usuário quer cadastrar mais algum número, se sim, adicione alguns contatos ao dicionário.

contatos = {
    "Ana": "1234-5678",
    "Pedro": "8765-4321",
    "Maria": "1357-2468"
}

while True:
    add_contato = input('Adicionar contato? (S para adicionar / N para encerrar): ')

    if add_contato == 'N':
        print('Programa encerrado.')
        break

    else:
        contatos[input('Nome: ')] = input('Número: ')
    
    print(contatos)
