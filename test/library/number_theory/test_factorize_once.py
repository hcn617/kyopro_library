import pytest

from library.number_theory.factorize_once import factorize_once


@pytest.mark.parametrize(
    "value, expected",
    [
        (1, []),  # empty case
        (5, [(5, 1)]),
        (6, [(2, 1), (3, 1)]),
        (1800, [(2, 3), (3, 2), (5, 2)]),
        (123456789012345678, [(2, 1), (3, 3), (21491747, 1), (106377431, 1)]),  # ~ 10^17
    ],
)
def test_factorize_once(value, expected):
    assert factorize_once(value) == expected
