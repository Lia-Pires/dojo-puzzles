import math

def primos_range(numero: int) -> list:
    lista_primos = []
    for numero in range(numero, 0):
        total_divisor = 0
        divisor = numero
        while divisor >= 1:
            resultado = numero/divisor
            if resultado%2 == 0:
                total_divisor += 1
        if total_divisor == 2:
            lista_primos.append(numero)

    return lista_primos


numero = int(input("Digite um número qualquer: "))
crivo_erastostenes = primos_range(math.floor(numero**(1/2)))

print(f'Os números primos até o limite {numero} são: {crivo_erastostenes}')