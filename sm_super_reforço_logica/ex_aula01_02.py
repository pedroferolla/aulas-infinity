ano = 1600

if ano % 400 == 0 or (ano % 400 == 0 and ano % 4 == 0):
    print('ano bissexto')


if (not ano % 4 and ano % 100) or (not ano % 400):
    print(f'O ano de {ano} é bissexto')

else:
    print(f'O ano de {ano} não é bissexto')
