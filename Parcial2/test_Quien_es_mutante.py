import pytest
from FuncionesP import *

# Prueba para la funcion is_mutant


@pytest.mark.parametrize("dna, expected_result", [

    ([
        "ATGCAA",
        "AGACCA",
        "ATCCGA",
        "ATTTAG",
        "TAGGAC",
        "ATTCCA"
    ], True),
    ([
        "ATGCGA",
        "CAGTGC",
        "TTCTCT",
        "AGAAGG",
        "CGCCTA",
        "TCACTA"
    ], False),

])
def test_is_mutant(dna, expected_result):
    result = is_mutant(dna)
    assert result == expected_result


# Prueba para la función is_valid_dna

@pytest.mark.parametrize("dna, expected_result", [
    ([
        "ATGCGA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCCTA",
        "TCACTG"
    ], True),
    ([
        "ATGCGA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCCTA",
        "TCACTX"
    ], False),
])
def test_is_valid_dna(dna, expected_result):
    result = is_valid_dna(dna)
    assert result == expected_result
