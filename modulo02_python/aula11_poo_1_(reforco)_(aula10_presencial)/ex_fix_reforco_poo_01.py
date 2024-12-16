# EXERCÍCIO DE FIXAÇÃO:

# 1 - Exercício de Elevador:
    # Crie uma classe Elevador.

    # Atributos:
        # piso_atual(int) - Começa no térreo (0)
        # total_pisos(int) - Representa o número total de pisos do prédio.

    # Métodos:
        # subir(pisos: int) - O elevador sobe uma quantidade de pisos.
        # descer(pisos: int) - O elevador desce uma quantidade de pisos.
        # ir_para_piso(piso: int) - O elevador vai diretamente para o piso especificado.
        # exibir_piso_atual() - Exibe o piso atual em que o elevador se encontra.

    # Comando para criar o objeto e chamar os métodos:
        # 1 - Crie um objeto da classe Elevador com 10 pisos.
        # 2 - Suba 3 pisos e exiba o piso atual.
        # 3 - Desça 2 pisos e exiba o piso atual.
        # 4 - Vá diretamente para o 5º piso e exiba o piso atual.

class Elevador:
    def __init__(self, total_pisos: int):
        self.piso_atual = 0
        self.total_pisos = total_pisos

    def subir(self, qnt_andares: int):
        andar_final = self.piso_atual + qnt_andares

        if andar_final > self.total_pisos:
            print(f'Não é possível subir {qnt_andares}')
        else:
            self.piso_atual = andar_final

    def descer(self, qnt_andares: int):
        andar_final = self.piso_atual - qnt_andares

        if andar_final >= 0:
            self.piso_atual = andar_final
        else:
            print(f'Não é possível descer {qnt_andares}')
        

elevador1 = Elevador(10)
print(elevador1.piso_atual)
elevador1.subir(6)
print(elevador1.piso_atual)
elevador1.subir(2)
print(elevador1.piso_atual)
