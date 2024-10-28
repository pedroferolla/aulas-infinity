# 3 - FIZZBUZZ
# Dificuldade: ***

# Objetivo: O jogador deve participar de uma contagem especial seguindo as regras do FizzBuzz.

# Descrição:
    # O programa começa a contar a partir de 1.
    # Se o número for múltiplo de 3, o jogador deve dizer "Fizz".
    # Se o número for múltiplo de 5, o jogador deve dizer "Buzz".
    # Se for múltiplo de ambos, deve dizer "FizzBuzz".
    # Se o número não for múltiplo nem de 3 e nem de 5, o usuário deverá digitar o próprio número.
    # O jogo termina se o jogador cometer um erro ou chegar a 35.

i = 1
print(i)

for i in range(1, 36):
    i += 1
    #fizz = i % 3 == 0                      |
    #buzz = i % 5 == 0                      | <----- DÚVIDA: por que não é possível atribuir as condicionantes às variáveis?
    #fizzbuzz = i % 3 == 0 and i % 5 == 0   |

    usuario = int(input('Próximo: '))
    if usuario != i:
        print(f'Errou! O próximo número é: {i}')
        break
    elif i % 3 == 0 and i % 5 == 0:
        print('FIZZBUZZ!')
    elif i % 3 == 0:
        print('FIZZ!')
    elif i % 5 == 0:
        print('BUZZ!')
    

# CONFERIR SE O ENUNCIADO E A EXECUÇÃO FORAM DEVIDAMENTE COMPREENDIDOS.
