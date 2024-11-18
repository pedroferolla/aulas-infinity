# Prova - Dicionários e Sets

# Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email.
# Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e 
# o endereço de email.
# Após coletar todas as informações, exiba o conteúdo do dicionário, mostrando todas as informações do contato 
# inserido pelo usuário.

contatos = {
    
}

while True:
    add_contato = input('\nAdicionar contato? (S para adicionar / N para encerrar): ')

    if add_contato == 'N':
        print('\nPrograma encerrado.')
        break

    elif add_contato == 'S':
        contatos[input('Nome: ')] = {'Telefone': input('Telefone: '), 'E-mail': input('E-mail: ')}
        
        print(contatos)

    else:
        print('\nOpção inválida.')
    
    