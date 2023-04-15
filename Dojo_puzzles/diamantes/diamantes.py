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

alfabeto = list(string.ascii_uppercase)
letra_digitada = input(f'Digite uma letra do alfaberto diferente de "A": ').upper()

espaco = " "
espaco_inicio = alfabeto.index(letra_digitada) + 1
espaco_meio = 0
lista_ate_letra_digitada = [
    letra
    for letra in alfabeto
    if alfabeto.index(letra) <= alfabeto.index(letra_digitada)
]

for letra in lista_ate_letra_digitada:
    espaco_inicio -= 1

    if letra == "A":
        print(f"{espaco * espaco_inicio}{letra}")
    else:
        espaco_meio += 2
        print(f"{espaco * espaco_inicio}{letra}{espaco * espaco_meio}{letra}")
    print()

lista_invertida = list(reversed(lista_ate_letra_digitada))
espaco_inicio = 1

for letra in lista_invertida:
    if lista_invertida.index(letra) != 0 and letra != "A":
        espaco_meio -= 2
        print(f"{espaco * espaco_inicio}{letra}{espaco * espaco_meio}{letra}")
        print()
        espaco_inicio += 1
    if letra == "A":
        print(f"{espaco * espaco_inicio}{letra}")


# alfabeto.index(letra_digitada.upper())
