from diamantes_funcoes import (
    base_diamante,
    topo_diamante,
    filtrar_alfabeto,
    inverter_lista,
)

letra_digitada = input(f'Digite uma letra do alfaberto diferente de "A": ').upper()

topo_diamante(filtrar_alfabeto(letra_digitada), letra_digitada)
base_diamante(inverter_lista(filtrar_alfabeto(letra_digitada)))
