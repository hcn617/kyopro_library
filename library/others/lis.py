from bisect import bisect_left


def longest_increasing_sequence(lst: list[int]) -> list[int]:
    """最長部分増加列

    Args:
        lst (list[int]): 対象となるリスト

    Returns:
        list[int]: 最長部分増加列の一例
    """
    INF = 1 << 63
    lis = [INF]
    for element in lst:
        idx = bisect_left(lis, element)
        lis[idx] = element
        if lis[-1] != INF:
            lis.append(INF)
    return lis[:-1]
