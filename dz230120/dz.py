from collections import deque


def unique_numbers(l: list) -> list:
    """
    Возвращение списка  всех неповторяющихся элемнтов входного списка
    """
    if not l:
        return []
    minel = min(l)
    maxel = max(l)
    m = [0] * ((maxel - minel) + 1)  # заполнили новый массив нулями
    # каждому элементу исходного массива находим место в новом, по формуле и прибавляем еденичку
    for el in l:
        m[el - minel] += 1
    rez = []
    # идём по исходному массиву и
    # если в новом массиве на его формульном месте число равно еденичке
    # то этот элемент встречается в исходном один раз
    for el in l:
        if m[el - minel] == 1:
            rez.append(el)

    return rez


def sort_stack(s: deque) -> None:
    """
    Сртировка стека с помощью дополнительных стеков
    """
    dop1 = deque()  # левая
    dop2 = deque()  # средняя
    dop3 = deque()  # правая

    while len(s)>0:
        l1 = s.pop()
        l2 = None
        while len(dop3) > 0:
            l2 = dop3.pop()
            if l1 <= l2:
                break
            else:
                dop1.append(l2)
                l2 = None
        if l2 is not None:
            dop3.append(l2)
        dop3.append(l1)
        while len(dop1) > 0:
            dop3.append(dop1.pop())

    while len(dop3)>0:
        dop2.append(dop3.pop())
    while len(dop2)>0:
        s.append(dop2.pop())
    


if __name__ == "__main__":
    # l = list(map(int, input().split()))
    # print(unique_numbers(l))
    s = deque([5, 4, 6, 1])
    sort_stack(s)
    print(s)
