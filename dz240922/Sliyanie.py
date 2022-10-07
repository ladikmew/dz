def Merge(left_List, right_List):
    i, j = 0, 0
    res = []
    while i < len(left_List) and j < len(right_List):
        if left_List[i] < right_List[j]:
            res.append(left_List[i])
            i = i + 1
        else:
            res.append(right_List[j])
            j = j + 1
    if i < len(left_List): res += left_List[i:]
    if j < len(right_List): res += right_List[j:]
    return res
def marge(List):
    size = len(List)
    if size == 1: return List
    mid = size // 2
    left_List = marge(List[:mid])
    right_List = marge(List[mid:])
    return Merge(left_List, right_List)
