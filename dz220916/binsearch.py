def bin_search(a, s):
    i = 0
    l = len(a)
    while l - i > 1:
        m:int = (l + i) // 2
        if a[m] > s:
            l = m
        else:
            i = m
    return i

def bin_search_2(a:list, s, i, l) -> int:
    m = (l + i) // 2
    if i == l - 1:
        return i
    elif a[m] > s:
        return bin_search_2(a, s, i, m)
    else:
        return bin_search_2(a, s, m, l)
