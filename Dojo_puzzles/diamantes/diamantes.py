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
letra_digitada = input(f"Digite uma letra qualquer: ").upper()

espaco = " "
espacos = alfabeto.index(letra_digitada) + 1
letra_anterior = None

for letra in alfabeto:
    espacos -= 1
    if alfabeto.index(letra) <= alfabeto.index(letra_digitada):
        if letra == "A":
            print(f"{espaco * espacos}{letra}")
            letra_anterior = letra
        else:
            meio = (
                (alfabeto.index(letra_anterior) + alfabeto.index(letra))
                if letra_anterior in alfabeto
                else espacos
            )
            print(f"{espaco * espacos}{letra}{espaco * meio}{letra}")
            letra_anterior = letra
    print()


# alfabeto.index(letra_digitada.upper())
