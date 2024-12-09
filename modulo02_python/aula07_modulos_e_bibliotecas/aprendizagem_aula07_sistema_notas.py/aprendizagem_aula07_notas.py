# APRENDIZAGEM

# 1 - SISTEMA DE NOTAS DE ALUNOS
    # Você vai criar um pequeno sistema que gerencia as notas dos alunos e calcula suas médias.

    # O sistema será divido em dois módulos:
        # 1 - Módulo 'notas.py': responsável por gerenciar as notas dos alunos.
        # 2 - Módulo 'relatorio.py': responsável por gerar e exibir relatórios de desempenho dos alunos.

    # O programa principal ('principal.py') usará funções desses dois módulos para adicionar notas, calcular médias e exibir 
    # relatórios.

    # Estrutura de arquivos:
        # meu_projeto/
        #    |--- principal.py
        #    |--- notas.py
        #    |--- relatorio.py

    # Estrutura dos módulos:
        # 1.1 - Módulo 'notas.py':
            # Função 'adicionar_nota()':
                # Recebe um aluno, uma nota e um dicionário de notas, em que cada chave é o nome do aluno e cada aluno 
                # (valor) tem uma lista de notas.

                # Depois que adicionar os alunos, implemente um código que, caso o aluno não esteja no dicionário, você o 
                # adiciona como uma chave nova.
                # E, caso o aluno já esteja, somente adicione a nota em sua lista de notas.

            # Função 'calcular_media()':
                # Recebe o aluno e um dicionário de notas.
                # Calcula a nota somente daquele aluno em específico.
                # Caso o aluno não tenha notas cadastradas, deverá retornar 'None'.

                    # calcular_media(alice, dicionario_notas)
                    # Deverá retornar 9.0, considerando que Alice tem 3 notas: 9.5, 10 e 7.5

            # Função 'listar_notas()':
                # Lista todas as notas de um aluno específico.
                # Os parâmetros serão o nome do aluno e o dicionário com todas as notas.

                # Considerando a Alice com notas 9.5, 7.5 e 10, a função deveria retornar:
                    # [9.5, 7.5, 10]

        # 1.2 - Módulo 'relatorio.py':
            # Função 'gerar_relatorio()':
                # Retorna uma string com as médias, conceitos e nomes de cada aluno.
                # Os conceitos seguem a tabela a seguir:
                    # Conceito   Média
                    #    A        > 9 
                    #    B       <= 9
                    #    C       <= 8
                    #    D       <= 7
                    #    E       <= 6
                    #    F       <= 4.5

            # Função 'exibir_relatorio()':
                # Apenas mostra na tela o relatório gerado pela função 'gerar_relatorio()':
                    # Aluno: Alice | Média: 9.00 | Conceito: B
                    # Aluno: Bob | Média: 8.60 | Conceito: B
                    # Aluno: Charlie | Média: 5.75 | Conceito: E

        # 1.3 - Arquivo 'principal.py':
            # Agora, vamos integrar as funções dos dois módulos para criar o sistema de gerenciamento de notas.
            # Você deverá iniciar o banco de notas como um dicionário vazio.
            # Cadastre as seguintes notas:
                # OBS: não pergunte para o usuário quais são as notas e os alunos, faça isso diretamente.
                # Aluno   Notas
                # Alice   8.5 e 7.0
                # Bob     9.0 e 6.5
                # Carol   10.0

            # Agora:
                # - Calcule a média da Alice, através da função 'calcular_media()';
                # - Liste as notas do Bob;
                # - Depois liste as notas da Carol;
                # - Exiba o relatório completo da turma
