from collections import deque
def unique_numbers(l: list) -> list:
    minel = 0
    maxel = 0
    m = []
    t = 10000000000000000
    t1 = -10000000000000000
    for i in range(len(l)): # находим минимальный и максимальный элементы массива
        if l[i] < t:
            t = l[i]
            minel = l[i]
        if l[i] > t1:
            t1 = l[i]
            maxel = l[i]
    for i in range((maxel - minel)+1):# заполнили новый массив нулями
        m.append(0)
    for i in range(len(l)):# каждому элементу исходного массива находим место в новом, по формуле и прибавляем еденичку
        f = int(l[i])-minel
        m[f] +=1
    rez = []
    for i in range(len(l)):# идём по исходному массиву и если в новом массиве на его формульном месте число равно еденичке то этот элемент встречается в исходном один раз
        if m[int(l[i])-minel]==1:
            rez.append(int(l[i]))

    return rez

def sort_stack(s: deque) -> None:




if __name__=="__main__":
    l = list(map(int,input().split()))
    print(unique_numbers(l))
    s = deque()
