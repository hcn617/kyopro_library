# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar

T = TypeVar("T")


class SortedSet(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                if not a or a[-1] != x:
                    a.append(x)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [
            a[n * i // num_bucket : n * (i + 1) // num_bucket]
            for i in range(num_bucket)
        ]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> tuple[list[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]:
                break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, b, i = self._position(x)
        if i != len(a) and a[i] == x:
            return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b : b + 1] = [a[:mid], a[mid:]]
        return True

    def _pop(self, a: list[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a:
            del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x:
            return False
        self._pop(a, b, i)
        return True

    def lt(self, x: T) -> T | None:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> T | None:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> T | None:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> T | None:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return a[i]
        else:
            for a in self.a:
                if i < len(a):
                    return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0:
                    return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a):
                    return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


class MexSet:
    _INF = 1 << 63

    def __init__(self) -> None:
        self._segset = SortedSet([(-self._INF, -self._INF), (self._INF, self._INF)])

    def contains(self, x: int) -> bool:
        """存在判定

        Args:
            x (int): このsetに含まれるかどうかを判定する値

        Returns:
            bool: 存在していればTrue
        """
        left_seg = self._segset.le((x, x))
        return left_seg[1] >= x

    def insert(self, x: int) -> bool:
        """挿入

        Args:
            x (int): 挿入する値

        Returns:
            bool: 既に存在していたらFalse, 新たに挿入されたらTrue
        """
        left_seg = self._segset.le((x, x))
        if left_seg[1] >= x or x == right_seg[0]:
            return False
        right_seg = self._segset.ge((x, x))
        if left_seg[1] + 1 == x == right_seg[0] - 1:
            self._segset.discard(left_seg)
            self._segset.discard(right_seg)
            self._segset.add((left_seg[0], right_seg[1]))
        elif left_seg[1] + 1 == x:
            self._segset.discard(left_seg)
            self._segset.add((left_seg[0], x))
        elif x == right_seg[0] - 1:
            self._segset.discard(right_seg)
            self._segset.add((x, right_seg[1]))
        else:
            self._segset.add((x, x))
        return True

    def discard(self, x: int) -> bool:
        """削除

        Args:
            x (int): 削除する値

        Returns:
            bool: 削除されればTrue, そもそもなければFalse
        """
        seg = self._segset.lt((x + 1, -self._INF))
        if seg[1] < x:
            return False
        if seg == (x, x):
            self._segset.discard(seg)
        elif seg[0] == x:
            self._segset.discard(seg)
            self._segset.add((x + 1, seg[1]))
        elif seg[1] == x:
            self._segset.discard(seg)
            self._segset.add((seg[0], x - 1))
        else:
            self._segset.discard(seg)
            self._segset.add((seg[0], x - 1))
            self._segset.add((x + 1, seg[1]))
        return True

    def ge(self, x: int) -> int:
        """x以上の最小の値

        Args:
            x (int): この値以上の最小の値を求める

        Returns:
            int: x以上の最小の値
        """
        seg = self._segset.lt((x + 1, -self._INF))
        if seg[1] >= x:
            return x
        nex_seg = self._segset.ge((x, x))
        return nex_seg[0]
