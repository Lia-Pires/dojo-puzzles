"""
Cada jogador deve dispor de uma área de 10x10 onde ele vai posicionar 5 navios 
de tamanhos diferentes: um porta-aviões (comprimento 5), um encouraçado 
(comprimento 4), um submarino e um destroyer (também de comprimento 3), 
e barco de patrulha (comprimento 2). Um jogador nunca deve saber a posição
dos navios do oponente. Os navios de um mesmo jogador não podem se cruzar e 
devem estar dentro das fronteiras da sua área disponível.

Depois que todas as peças estão posicionadas, os jogadores se alternam em 
turnos para lançar bombas sobre o outro oponente especificando qual posição 
ele deseja atacar. Se algum dos navios do jogador que está sendo atacado estiver 
na posição atacada, considera-se que o navio foi atingido. O ataque falha se o 
atacante lançar uma bomba em um local onde não existe nenhum navio do oponente.

Caso todos as posições de um navio for atingida, o jogador atacado deve informar 
o oponente qual dos seus navios afundou. O jogo continua até que um jogador 
afunde todos os navios de seu oponente; este jogador é então considerado vencedor.

Você deve desenvolver um programa que jogue uma partida de batalha naval 
entre dois oponentes. Você precisa:

Definir uma maneira de indicar o estado inicial dos navios dos jogadores;
Exibir todos os movimentos dos jogadores, informando se os ataques 
foram bem sucedidos ou não;
Informar quando um navio é atingido e quando ele é afundado;
Exibir ao final do jogo um mapa final do posicionamento final dos navios 
dos jogadores.
"""
from typing import Type


# Em andamento
class Tabuleiro:
    def __init__(self):
        A = [0, 1, 2, 3, 4]
        B = [0, 1, "a", 3, 4]
        C = [0, 1, "a", 3, 4]
        D = [0, 1, "a", 3, 4]
        E = [0, 1, "a", 3, 4]

        self.tabuleiro = [A, B, C, D, E]

    # TODO: colocar o tipo de jogador nas annotations
    def verificar_espacos(lista: list, jogador) -> bool:
        verificacao = []
        for itens in lista:
            if type(jogador.tabuleiro[itens[0]][itens[1]]) == int:
                pass
            else:
                print("O espaço já está sendo ocupado, tente novamente!")
                return False
        return True

    def posicionar_porta_avioes(
        jogador,
        num1: int,
        num2: int,
        num3: int,
        num4: int,
        num5: int,
        num6: int,
        num7: int,
        num8: int,
        num9: int,
        num10: int,
    ):
        lista = [[num1, num2], [num3, num4], [num5, num6], [num7, num8], [num9, num10]]

        if Tabuleiro.verificar_espacos(lista, jogador):
            for itens in lista:
                jogador.tabuleiro[itens[0]][itens[1]] = "p.a"

    def posicionar_encouracado(
        jogador,
        num1: int,
        num2: int,
        num3: int,
        num4: int,
        num5: int,
        num6: int,
        num7: int,
        num8: int,
    ):
        lista = [[num1, num2], [num3, num4], [num5, num6], [num7, num8]]

        if Tabuleiro.verificar_espacos(lista, jogador):
            for itens in lista:
                jogador.tabuleiro[itens[0]][itens[1]] = "enc"

    def posicionar_submarino(
        jogador, num1: int, num2: int, num3: int, num4: int, num5: int, num6: int
    ):
        lista = [[num1, num2], [num3, num4], [num5, num6]]

        if Tabuleiro.verificar_espacos(lista, jogador):
            for itens in lista:
                jogador.tabuleiro[itens[0]][itens[1]] = "sub"

    def posicionar_destroyer(
        jogador, num1: int, num2: int, num3: int, num4: int, num5: int, num6: int
    ):
        lista = [[num1, num2], [num3, num4], [num5, num6]]

        if Tabuleiro.verificar_espacos(lista, jogador):
            for itens in lista:
                jogador.tabuleiro[itens[0]][itens[1]] = "des"

    def posicionar_barco_patrulha(jogador, num1: int, num2: int, num3: int, num4: int):
        lista = [[num1, num2], [num3, num4]]

        if Tabuleiro.verificar_espacos(lista, jogador):
            for itens in lista:
                jogador.tabuleiro[itens[0]][itens[1]] = "b.p"

    def organizar_tabuleiro(jogador):
        print(
            "Digite os os índices de um tabuleiro 10x10 onde quer posicionar suas peças (LxC)!"
        )
        print("Tabuleiro inicial: ")
        for indice in jogador.tabuleiro:
            print(indice)

        num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = map(
            int, input("Porta aviões, comprimento 5: ").split(",")
        )
        Tabuleiro.posicionar_porta_avioes(
            jogador, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10
        )

        num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = map(
            int, input("Encouraçado, comprimento 4: ").split(",")
        )
        Tabuleiro.posicionar_encouracado(
            jogador, num1, num2, num3, num4, num5, num6, num7, num8
        )

        num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = map(
            int, input("Destroyer, comprimento 3: ").split(",")
        )
        Tabuleiro.posicionar_destroyer(jogador, num1, num2, num3, num4, num5, num6)

        um1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = map(
            int, input("Submarino, comprimento 3: ").split(",")
        )
        Tabuleiro.posicionar_submarino(jogador, num1, num2, num3, num4, num5, num6)

        num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = map(
            int, input("Barco Patrulha, comprimento 2: ").split(",")
        )
        Tabuleiro.posicionar_barco_patrulha(jogador, num1, num2, num3, num4)

        print("Tabuleiro Final: ")
        for indice in jogador.tabuleiro:
            print(indice)

    def tabuleiro_oponente(oponente):
        print("Escolha o índice onde quer atacas (LxC):")
        print("  0, 1, 2, 3, 4")
        ind = 0
        for indice in jogador_1.tabuleiro:
            print(f"{ind} [*, *, *, *, *]")
            ind += 1

    def atacar_oponente(oponente, num1, num2):
        if type(oponente.tabuleiro[num1][num2]) != int:
            print(f"Você atingiu uma parte do {oponente.tabuleiro[num1][num2]}")
            oponente.tabuleiro[num1][num2] = 0
        else:
            print("Você não atingiu seu oponente, aguarde a próxima rodada.")


jogador_1 = Tabuleiro()
jogador_2 = Tabuleiro()


#     Tabuleiro.posicionar_barco_patrulha(jogador_1, 1, 1, 3, 4)

#     Tabuleiro.posicionar_encouracado(jogador_1, 1, 2, 3, 4, 1, 2, 3, 4)
#     Tabuleiro.posicionar_submarino(jogador_1, 1, 2, 3, 4, 1, 2)


# Tabuleiro.posicionar_porta_avioes(jogador_1, 0, 0, 0, 1, 0, 2, 0, 3, 0, 4)
# Tabuleiro.posicionar_barco_patrulha(jogador_1, 1, 1, 3, 4)
# Tabuleiro.posicionar_destroyer(jogador_1, 1, 2, 3, 1, 2, 3)
# Tabuleiro.posicionar_encouracado(jogador_1, 1, 2, 3, 4, 1, 2, 3, 4)
# Tabuleiro.posicionar_submarino(jogador_1, 1, 2, 3, 4, 1, 2)

# for indice in jogador_1.tabuleiro:
#     print(indice)

print("  0, 1, 2, 3, 4")
ind = 0
for indice in jogador_1.tabuleiro:
    print(f"{ind} [*, *, *, *, *]")
    ind += 1
