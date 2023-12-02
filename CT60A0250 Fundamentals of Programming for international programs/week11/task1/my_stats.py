def my_mean(L: list) -> float:
    return sum(L) / len(L)


def my_variance(L: list) -> float:
    return sum((x - my_mean(L))**2 for x in L) / len(L)


def my_mode(L: list) -> float:
    return max(L, key=L.count)
