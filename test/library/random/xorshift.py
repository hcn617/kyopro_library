import pytest

from library.random.xorshift import Xorshift32, Xorshift64


@pytest.mark.parametrize(
    "seed",
    [
        2,
        303,
        23948539,
    ],
)
def test_xorshift32_same_seed(seed):
    rng1 = Xorshift32(seed)
    rng2 = Xorshift32(seed)
    for _ in range(100):
        assert rng1.next() == rng2.next()


@pytest.mark.parametrize(
    "seed",
    [
        1,
        5938,
        7714801932196503346,
    ],
)
def test_xorshift64_same_seed(seed):
    rng1 = Xorshift64(seed)
    rng2 = Xorshift64(seed)
    for _ in range(100):
        assert rng1.next() == rng2.next()
