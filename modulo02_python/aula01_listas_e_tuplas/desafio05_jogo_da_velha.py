# DESAFIOS
# 5 - Jogo da velha
# Dificuldade: *****

# 1 - Preparar tabuleiro:
    # 1 - Crie uma lista para representar o tabuleiro do jogo. Inicialmente, essa lista deve conter 9 posições, 
        #  todas vazias (por exemplo, representadas por espações em branco).
    # 2 - Defina uma variável para armazenar qual jogador está fazendo a jogada.
        # O jogo começará com o jogador 'X'.
    # 3 - Defina uma variável que indique se o jogo está ativo. Inicialmente, o jogo está ativo.

# 2 - Exibir o tabuleiro:
    # 1 - Crie um loop que percorre a lista do tabuleiro e imprime as posições do tabuleiro em formato de 3 linhas 
        # e 3 colunas, separadas por barras verticais (|).
    # 2 - Adicione linhas horizontais entre as linhas do tabuleiro para uma melhor visualização, 
        # exceto após a última linha.

# 3 - Solicitar a jogada do jogador:
    # 1 - Peça ao jogador atual para escolher uma posição no tabuleiro (de 1 a 9).
    # 2 - Converta a escolha do jogador para o índice correspondente na lista do tabuleiro (subtraindo 1 
        # do número escolhido).
    # 3 - Verifique se a posição escolhida está vazia. Se estiver ocupada, peça ao jogador para escolher 
        # outra posição. Se estiver vazia, atualize o tabuleiro com a jogada do jogador.

# 4 - Verificar condições de vitória:
    # 1 - Defina as condições de vitória: chegue a um resultado vencedor, verificando todas as possíveis linhas, 
        # colunas e diagonais no tabuleiro.
    # 2 - Cheque se há uma combinação vencedora no tabuleiro. Se encontrar, declare o jogador atual como vencedor e 
        # termine o jogo.

# 5 - Verificar empate:
    # 1 - Verifique se todas as posições do tabuleiro estão preenchidas e se não há um vencedor.
    # 2 - Declare um empate se o tabuleiro estiver completamente preenchido e não houver um vencedor.

# 6 - Alternar jogador:
    # 1 - Troque o jogador atual para o próximo jogador (de 'X' para 'O' e vice-versa).
    # 2 - Continue com o próximo turno até que o jogo termine (seja por vitória ou empate).