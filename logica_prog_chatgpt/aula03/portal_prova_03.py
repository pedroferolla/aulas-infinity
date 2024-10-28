# Prova Estrutura de repetição: WHILE

# Você está criando um programa em Python para simular um jogo simples de adivinhação.
# O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar.
# O jogador terá até 3 tentativas para acertar o número.
# Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou
# atingir o limite de tentativas.
# Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo
# caso as 3 tentativas se esgotem sem sucesso.

numero = 7
tentativas = 0
tentativas_max = 3

while tentativas < tentativas_max:
    palpite = int(input('Tente adivinhar o número: '))
    tentativas += 1

    if palpite == numero:
        print('Certa resposta!')
        break
    else:
        print('Errou!')

    if tentativas == tentativas_max:
        print('GAME OVER')
