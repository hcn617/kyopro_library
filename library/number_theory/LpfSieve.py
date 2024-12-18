class LpfSieve:
    _lpf_list: list[int]

    def __init__(self, max_value: int) -> None:
        self._lpf_list = [0] * (max_value + 1)
        self._lpf_list[0] = 0
        self._lpf_list[1] = 1
        for i in range(2, max_value + 1):
            if self._lpf_list[i] == 0:
                for j in range(i, max_value + 1, i):
                    if self._lpf_list[j] == 0:
                        self._lpf_list[j] = i

    def lpf(self, value: int) -> int:
        """最小の素因数を返す

        Args:
            value (int): 対象の数

        Returns:
            int: 最小の素因数
        """
        return self._lpf_list[value]
    
    def is_prime(self, value: int) -> bool:
        """素数かどうかを返す

        Args:
            value (int): 対象の数

        Returns:
            bool: 素数ならTrue, そうでないならFalse
        """
        if value < 2:
            return False
        return self._lpf_list[value] == value
    
    def factorize(self, value: int) -> list[tuple[int, int]]:
        """素因数分解

        Args:
            value (int): 対象の数

        Returns:
            list[tuple[int, int]]: 素因数とその個数のリスト
        """
        x = value
        divisor_count_list: list[tuple[int, int]] = []
        while x > 1:
            divisor = self._lpf_list[x]
            div_count = 0
            while x % divisor == 0:
                x //= divisor
                div_count += 1
            divisor_count_list.append((divisor, div_count))
        return divisor_count_list
    
    def divisors(self, value: int) -> list[int]:
        """約数列挙

        Args:
            value (int): 対象の数

        Returns:
            list[int]: 約数のリスト
        """
        divisor_list = [1]
        for divisor, count in self.factorize(value):
            new_divisor_list = []
            for d in divisor_list:
                for _ in range(count):
                    d *= divisor
                    new_divisor_list.append(d)
            divisor_list.extend(new_divisor_list)
        return divisor_list
