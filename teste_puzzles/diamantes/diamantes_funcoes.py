"""
Dado uma letra ('A' a 'Z'), exiba um diamante iniciando em 'A' e tendo a letra 
fornecida com o ponto mais distante.
                                                                                
Por exemplo, dado a letra 'E' temos:

    A   

   B B

  C   C

 D     D

E       E 

 D     D 

  C   C

   B B

    A

 

Dado a letra 'C' temos:

  A

 B B

C   C

 B B

  A

"""

import string

espaco = " "
espaco_meio = 0


def filtrar_alfabeto(letra_digitada: str) -> list:
    """Retorna uma lista do alfabeto até a letra recebida"""
    alfabeto = list(string.ascii_uppercase)
    lista_filtrada = [
        letra
        for letra in alfabeto
        if alfabeto.index(letra) <= alfabeto.index(letra_digitada)
    ]
    return lista_filtrada


def inverter_lista(lista: list) -> list:
    """Recebe uma lista e retorna a mesma lista invertida"""
    lista_invertida = list(reversed(lista))
    return lista_invertida


def topo_diamante(lista_filtrada: list, letra_digitada: list) -> None:
    """Gera o topo do diamante de letras recebendo a
    lista já filtrada e a letra que foi escolhida"""
    global espaco_meio
    espaco_inicio = lista_filtrada.index(letra_digitada) + 1
    for letra in lista_filtrada:
        espaco_inicio -= 1
        if letra:
            if letra == "A":
                print(f"{espaco * espaco_inicio}{letra}")
            else:
                espaco_meio += 2
                print(f"{espaco * espaco_inicio}{letra}{espaco * espaco_meio}{letra}")
            print()


def base_diamante(lista_invertida: list) -> None:
    """Gera a base do diamante de letra recebendo a lista
    que foi usada na função topo_diamante, porém invertida"""
    global espaco_meio
    espaco_inicio = 1
    for letra in lista_invertida:
        if lista_invertida.index(letra) != 0 and letra != "A":
            espaco_meio -= 2
            print(f"{espaco * espaco_inicio}{letra}{espaco * espaco_meio}{letra}")
            print()
            espaco_inicio += 1
        if letra == "A":
            print(f"{espaco * espaco_inicio}{letra}")
