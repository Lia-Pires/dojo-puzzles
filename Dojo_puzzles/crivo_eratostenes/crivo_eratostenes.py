"""
o Crivo de Eratóstenes é um método que permite obter uma tabela de números primos 
até um limite escolhido(n): Escreva uma lista de números de 2 até n, 2 é o menor 
número primo logo retire da lista todos os seus múltiplos, agora o segundo número 
da lista (o 3) será um número primo retire todos os números da lista que sejam 
múltiplos deste, agora o terceiro número da lista será um número primo (o 5); 
Repita o processo elimine da lista todos os múltiplos desde, e vá para o próximo 
número. Repita esses passos até o número correspondente a raiz de n, arredondada 
para baixo, exemplo, quer se saber todos os números primos entre 1 e 30, logo 
o processo continuará até 30^(1/2) = 5.47 pega se apenas a parte inteira logo 
obtemos 5. (floor(sqrt(30))) => ⌊√30⌋
"""
from math import sqrt, floor


def primos_range(numero: int) -> list:
    numero = floor(sqrt((numero)))
    lista_primos = []
    for numero in range(numero, 1, -1):
        total_divisor = 0
        divisor = numero + 1
        while divisor >= 1:
            divisor -= 1
            if divisor != 0 and numero % divisor == 0:
                total_divisor += 1
        if total_divisor == 2:
            lista_primos.append(numero)

    return lista_primos


crivo_erastostenes = primos_range(20)

print(f"Os números primos até o limite √20 são: {crivo_erastostenes}")


# numero = int(input("Digite um número inteiro qualquer: "))
# crivo_erastostenes = primos_range(floor(sqrt((numero))))

# print(f"Os números primos até o limite {numero} são: {crivo_erastostenes}")
