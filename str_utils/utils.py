def reverse_string_slicing(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError

    return s[::-1]


def reverse_string_swap(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError

    if len(s) <= 1:
        return s

    s_list = list(s)
    for i in range(len(s_list) // 2):
        s_list[i], s_list[len(s) - 1 - i] = s_list[len(s) - 1 - i], s_list[i]

    return ''.join(s_list)
