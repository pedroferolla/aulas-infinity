# EXERCÍCIOS DE FIXAÇÃO - PARTE 2/2

# 6 - Utilize o exercício anterior e implemente uma lógica para buscar o telefone de um contato específico 
    # através do nome da pessoa.

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


print(contatos[input('\nPara buscar um contato, digite o nome: ')])
