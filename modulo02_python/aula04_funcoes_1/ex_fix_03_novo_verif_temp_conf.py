# EXERCÍCIOS DE FIXAÇÃO

# 3 - Verificação de Temperatura no Conforto
    # Problema: em um dia quente de verão, você quer saber se o ambiente está confortável ou não, de acordo com a 
    # temperatura externa.
    # Crie uma função que diga se a temperatura está dentro de uma faixa de conforto (digamos, entre 18ºC e 25ºC).

    # Exemplo de entrada:
    # Temperatura: 30ºC

    # Exemplo de saída:
    # A temperatura está fora da zona de conforto.

def temperatura_conforto(celsius: int):
    if celsius >= 18 and celsius <= 25:
        mensagem = 'A temperatura está dentro da zona de conforto.'
    elif celsius < 18 or celsius > 25:
        mensagem = 'A tempertatura está fora da zona de conforto.'

    return mensagem

print(temperatura_conforto(int(input('Temperatura (ºC): '))))

