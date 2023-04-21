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


class Jogo:
    navios = {
        "p.a": "Porta-Aviões",
        "enc": "Encouraçado",
        "sub": "Submarino",
        "des": "Destroyer",
        "b.p": "Barco de Patrulha",
    }

    def __init__(self, nome):
        A = ["b.p", 0, 0, 0, 0]
        B = [0, 0, 0, 0, 0]
        C = [0, 0, 0, 0, 0]
        D = [0, 0, 0, 0, 0]
        E = [0, 0, 0, 0, 0]

        self.nome = nome
        self.tabuleiro = [A, B, C, D, E]

    # TODO: colocar o tipo de jogador nas annotations
    def verificar_espacos(lista: list, jogador) -> bool:
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

        if Jogo.verificar_espacos(lista, jogador):
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

        if Jogo.verificar_espacos(lista, jogador):
            for itens in lista:
                jogador.tabuleiro[itens[0]][itens[1]] = "enc"

    def posicionar_submarino(
        jogador, num1: int, num2: int, num3: int, num4: int, num5: int, num6: int
    ):
        lista = [[num1, num2], [num3, num4], [num5, num6]]

        if Jogo.verificar_espacos(lista, jogador):
            for itens in lista:
                jogador.tabuleiro[itens[0]][itens[1]] = "sub"

    def posicionar_destroyer(
        jogador, num1: int, num2: int, num3: int, num4: int, num5: int, num6: int
    ):
        lista = [[num1, num2], [num3, num4], [num5, num6]]

        if Jogo.verificar_espacos(lista, jogador):
            for itens in lista:
                jogador.tabuleiro[itens[0]][itens[1]] = "des"

    def posicionar_barco_patrulha(jogador, num1: int, num2: int, num3: int, num4: int):
        lista = [[num1, num2], [num3, num4]]

        if Jogo.verificar_espacos(lista, jogador):
            for itens in lista:
                jogador.tabuleiro[itens[0]][itens[1]] = "b.p"

    def organizar_tabuleiro(jogador):
        print(
            f"{jogador.nome} digite os os índices de um tabuleiro 10x10 onde quer posicionar suas peças (LxC)!\n"
        )
        print("Tabuleiro inicial: \n")
        ind = 0
        print("  0, 1, 2, 3, 4")
        for indice in jogador.tabuleiro:
            print(f"{ind}{indice}")
            ind += 1

        num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = map(
            int, input("Porta aviões, comprimento 5: ").split(",")
        )
        Jogo.posicionar_porta_avioes(
            jogador, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10
        )

        num1, num2, num3, num4, num5, num6, num7, num8 = map(
            int, input("Encouraçado, comprimento 4: ").split(",")
        )
        Jogo.posicionar_encouracado(
            jogador, num1, num2, num3, num4, num5, num6, num7, num8
        )

        num1, num2, num3, num4, num5, num6 = map(
            int, input("Destroyer, comprimento 3: ").split(",")
        )
        Jogo.posicionar_destroyer(jogador, num1, num2, num3, num4, num5, num6)

        num1, num2, num3, num4, num5, num6 = map(
            int, input("Submarino, comprimento 3: ").split(",")
        )
        Jogo.posicionar_submarino(jogador, num1, num2, num3, num4, num5, num6)

        num1, num2, num3, num4 = map(
            int, input("Barco Patrulha, comprimento 2: ").split(",")
        )
        Jogo.posicionar_barco_patrulha(jogador, num1, num2, num3, num4)

        print("Tabuleiro Final: ")
        for indice in jogador.tabuleiro:
            print(indice)
        print()

    def tabuleiro_oponente(oponente):
        print("Escolha o índice onde quer atacas (LxC):")
        print("  0, 1, 2, 3, 4")
        ind = 0
        for indice in oponente.tabuleiro:
            print(f"{ind} [*, *, *, *, *]")
            ind += 1

    def atacar_oponente(oponente, num1, num2):
        if type(oponente.tabuleiro[num1][num2]) != int:
            atingido = oponente.tabuleiro[num1][num2]
            print(f"Você atingiu uma parte do {Jogo.navios.get(atingido)}")
            oponente.tabuleiro[num1][num2] = 0
            Jogo.verificar_navio_afundado(atingido, oponente)
        else:
            print("Você não atingiu seu oponente, aguarde a próxima rodada.")

    def verificar_fim_partida(jogador):
        for lista in jogador.tabuleiro:
            fim = all(isinstance(item, int) for item in lista)
            if fim == False:
                return False
            else:
                pass
        return True

    def verificar_navio_afundado(atingido, oponente):
        navio = any(atingido in sublista for sublista in oponente.tabuleiro)
        if navio:
            pass
        else:
            navio_afundado = Jogo.navios.get(atingido)
            print(f"Você afundou o {navio_afundado}")

    def jogo(nome1, nome2):
        jogador_1 = Jogo(nome1)
        jogador_2 = Jogo(nome2)

        Jogo.organizar_tabuleiro(jogador_1)
        Jogo.organizar_tabuleiro(jogador_2)

        fim = Jogo.verificar_fim_partida(jogador_2)
        fim2 = Jogo.verificar_fim_partida(jogador_1)

        while not (fim or fim2):
            print("A Partida Continua, próxima rodada. ")
            print(f"Vez do {jogador_1.nome}")
            Jogo.tabuleiro_oponente(jogador_2)
            num1 = int(input("Linha: "))
            num2 = int(input("Coluna: "))
            Jogo.atacar_oponente(jogador_2, num1, num2)
            fim2 = Jogo.verificar_fim_partida(jogador_2)
            if fim2:
                print(f"A partida chegou ao fim!, {jogador_1.nome} venceu!")
                break

            print(f"Vez do {jogador_2.nome}")
            Jogo.tabuleiro_oponente(jogador_1)
            num1 = int(input("Linha: "))
            num2 = int(input("Coluna: "))
            Jogo.atacar_oponente(jogador_1, num1, num2)
            fim = Jogo.verificar_fim_partida(jogador_1)
            if fim:
                print(f"A partida chegou ao fim!, {jogador_2.nome} venceu!")
                break

        print("Final: ")
        print(f"Jogador 1: {jogador_1.nome}")
        print("  0, 1, 2, 3, 4")
        for indice in jogador_1.tabuleiro:
            print(f"{ind}{indice}")
            ind += 1

        print(f"Jogador 2: {jogador_2.nome}")
        print("  0, 1, 2, 3, 4")
        for indice in jogador_2.tabuleiro:
            print(f"{ind}{indice}")
            ind += 1
