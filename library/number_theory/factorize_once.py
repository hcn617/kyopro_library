def factorize_once(value: int) -> list[tuple[int, int]]:
    """素因数分解

    Args:
        value (int): 素因数分解する数

    Returns:
        list[tuple[int, int]]: 素因数とその個数のリスト
    
    Notes:
        計算量はO(√n)
    """
    x = value
    divisor = 2
    divisor_count_list: list[tuple[int, int]] = []
    while divisor**2 <= x:
        div_count = 0
        while x % divisor == 0:
            x //= divisor
            div_count += 1
        if div_count >= 1:
            divisor_count_list.append((divisor, div_count))
        divisor += 1
    if x > 1:
        divisor_count_list.append((x, 1))
    return divisor_count_list
