import pytest

from library.string.rollinghash import RollingHash


@pytest.mark.parametrize(
    "s, sl, sr, t, tl, tr, expected",
    [
        ("abcd", 0, 4, "abcd", 0, 4, True),
        ("abcd", 0, 3, "dabc", 1, 4, True),
        ("abcde", 1, 4, "ebcda", 1, 4, True),
        ("abcd", 0, 4, "abce", 0, 4, False),
        ("abcd", 1, 1, "fghi", 2, 2, True),
    ],
)
def test_rollinghash(
    s: str, sl: int, sr: int, t: str, tl: int, tr: int, expected: bool
) -> None:
    rh_s = RollingHash(s)
    rh_t = RollingHash(t)
    result = rh_s.get(sl, sr) == rh_t.get(tl, tr)
    assert result == expected
