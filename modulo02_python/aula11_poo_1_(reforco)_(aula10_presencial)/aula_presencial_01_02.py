def teste_se_e_menor_de_idade(nome: str, idade: int):
    if idade < 18:
        print(f'A pessoa {nome} é menor de idade.')

    else:
        print(f'A pessoa {nome} é maior de idade.')


pessoa1 = 'Cleiton'
idade1 = 30
e_menor = False

# if idade1 < 18:
#     print(f'O {pessoa1} é menor de idade')
#     e_menor = True
# else:
#     print(f'O {pessoa1} é maior de idade')
#     e-e_menor = False

teste_se_e_menor_de_idade(pessoa1, idade1)


pessoa2 = 'Sara'
idade2 = 14
e_menor2 = False

# if idade2 < 18:
#     print(f'A {pessoa2} é menor de idade')
#     e_menor2 = True
# else:
#     print(f'A {pessoa2} é maior de idade')
#     e_menor2 = False

teste_se_e_menor_de_idade(pessoa2, idade2)
