with open('27-B.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
max_sum = -10000000
max_3k = -1000000000
m_2, m_1 = sorted(a[:3 * k])[-2:]

for i in range(3 * k, len(a)):
    max_3k = max(max_3k, a[i - 3 * k])
    if m_1 != max_3k:
        max_sum = max(max_sum, m_1 + max_3k + a[i])

    else:
        max_sum = max(max_sum, m_2 + max_3k + a[i])

    g, m_2, m_1 = sorted([m_1, m_2, a[i]])

print(max_sum)
#214796 21506