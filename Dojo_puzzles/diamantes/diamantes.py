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
# letra_digitada = input(f"Digite uma letra qualquer: ").upper()
letra_digitada = "Z"

espaco = " "
espacos = alfabeto.index(letra_digitada) + 1
letra_anterior = None
lista_ate_digitada = [
    letra
    for letra in alfabeto
    if alfabeto.index(letra) <= alfabeto.index(letra_digitada)
]

for letra in lista_ate_digitada:
    espacos -= 1

    if letra == "A":
        print(f"{espaco * espacos}{letra}")
        letra_anterior = letra
    else:
        meio = (
            (lista_ate_digitada.index(letra_anterior) + lista_ate_digitada.index(letra))
            if letra_anterior in lista_ate_digitada
            else espacos
        )
        print(f"{espaco * espacos}{letra}{espaco * meio}{letra}")
        letra_anterior = letra
    print()

lista_invertida = list(reversed(lista_ate_digitada))
espacos = alfabeto.index(letra_digitada) + 1
espacos = 1

for letra in lista_invertida:
    if lista_invertida.index(letra) != 0 and letra != "A":
        meio -= 2
        print(f"{espaco * espacos}{letra}{espaco * meio}{letra}")
        print()
        espacos += 1
    if letra == "A":
        print(f"{espaco * espacos}{letra}")


# alfabeto.index(letra_digitada.upper())
