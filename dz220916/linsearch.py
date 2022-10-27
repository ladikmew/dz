
def lin_search(a: list, s):
    for i, el in enumerate(a):
        if el == s:
            return i


def search_fl(a: list(float), s: float) -> int:
    for i, el in enumerate(a):
        if el-s <= 0.001 or s-el <= 0.001:
            return i
