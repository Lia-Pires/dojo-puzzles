import pytest
from pytest import mark

from Dojo_puzzles.crivo_eratostenes.crivo_eratostenes import primos_range


@mark.parametrize(
    "parametro, resultado_eperado",
    [(10, [3, 2]), (20, [3, 2]), (30, [5, 3, 2]), (1, []), (100, [7, 5, 3, 2])],
)
def test_primos_range(parametro, resultado_eperado):
    assert primos_range(parametro) == resultado_eperado
