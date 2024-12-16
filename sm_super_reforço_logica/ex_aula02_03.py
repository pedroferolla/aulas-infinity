# Link do desafio https://1drv.ms/b/s!Avy8iION82gso_g5_V4dBjmlyUe45Q

# Mandar resposta em anexo para o e-mail 
# walterinfinity@outlook.com

# Junto com nome completo e turma

# https://dontpad.com/desafioDoWalter

# printe todos os nomes com mais de 6 caracteres :

lista = [['Ximiun','Yakborgob','Gefoouil','Zoetuso' ],
['Cawao', 'Tarfeura', 'Haykui', 'Esuma' ],
['Dauceyarn', 'Harriric', 'Celeblyaborn', 'Khadpu' ],
['Hayla', 'Diono', 'Olficiolu', 'Venbou']] 

#lista contendo outras listas

for lista in lista:
    for nome in lista:
        if len(nome) > 6:
            print(nome)
