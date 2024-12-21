import pytest

from library.others.lis import longest_increasing_sequence


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1]),
        ([1, 2, 3, 2, 4, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_lis(lst: list[int], expected: list[int]) -> None:
    assert longest_increasing_sequence(lst) == expected
