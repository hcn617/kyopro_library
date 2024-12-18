class Xorshift32:
    MASK = 0xFFFFFFFF

    def __init__(self, seed: int = 2864813732, *, real_random: bool = False) -> None:
        if real_random:
            import random

            seed = random.getrandbits(32)

        self.state = seed & self.MASK

    def next(self) -> int:
        self.state ^= self.state << 13
        self.state ^= self.state >> 17
        self.state ^= self.state << 5
        return self.state & self.MASK


class Xorshift64:
    MASK = 0xFFFFFFFFFFFFFFFF

    def __init__(
        self, seed: int = 7714801932196503346, *, real_random: bool = False
    ) -> None:
        if real_random:
            import random

            seed = random.getrandbits(64)

        self.state = seed & self.MASK

    def next(self) -> int:
        self.state ^= self.state << 7
        self.state ^= self.state >> 9
        return self.state & self.MASK
