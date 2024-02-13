def power(n: int, b: int = 2) -> int:
    """
    Raises the number n to the power of b.
    :param n: Number
    :param b: Power base (default: 2)
    :return: Integer - result of raising
    """
    res = 1
    for i in range(b):
        res *= n
    return res


def union_str(str_list: list) -> str:
    string = ""
    for i in range(len(str_list)):
        string += str_list[i] + ', '
    return string


s2 = power(2, 6)
print(s2)
