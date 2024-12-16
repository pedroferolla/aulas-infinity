esta_frio = True
esta_quente = True
tenho_dinheiro = True
vai_chover = True

if tenho_dinheiro:
    if esta_frio:
        print('levar casaco')
    else:
        if esta_quente:
            print('levar camiseta')
        else:
            print('sair de camisa')
else:
    print('fica em casa')


if not tenho_dinheiro:
    print('fica em casa')
elif esta_frio:
    print('levar casaco')
elif esta_quente:
    print('levar camiseta')
else:
    print('levar camisa')
    

if vai_chover:
    print('levar guarda chuva')




