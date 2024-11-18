# EXERCÍCIOS DE FIXAÇÃO

# 4 - Filtro de Emails
    # Crie uma função chamada 'filtrar_emails', que recebe uma lista de e-mails e retorna uma lista com os e-mails 
    # que contêm o domínio '@gmail.com'.

    # Exemplo:
    # lista_emails = ['teste@gmail.com', 'info@yahoo.com', 'contato@gmail.com']

    # emails_filtrados = filtrar_emails(lista_emails)
    # Deve retornar ['teste@gmail.com, 'contato@gmail.com']

lista_emails = ['teste@gmail.com', 'info@yahoo.com', 'contato@gmail.com']
emails_filtrados = []

def filtrar_emails(lista_emails):
    for email in lista_emails:
        if '@gmail.com' in email:
            emails_filtrados.append(email)
        
    return emails_filtrados

print(filtrar_emails(lista_emails))
