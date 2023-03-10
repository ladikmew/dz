def search_min(a, start):
    m = a[start]
    min_i = start
    for i in range(start, len(a)):
        if a[i] < m:
            m = a[i]
            min_i = i
    return min_i


def sort_vi(a):
    for i in range(len(a) - 1):
        m_i = search_min(a, i)
        a[i], a[m_i] = a[m_i], a[i]
    return a
