n = int(input())
a = []
count = 0
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
        if row[i] == 1:
            count += 1
    a.append(row)


def dfs(graph, start, visited):
    if visited is None:
        visited = set()
    visited.append(start)
    for n in graph[start]:
        if not n in visited:
            dfs(graph, n, visited)
    return visited


if __name__ == "__main__":
    k = []
    g = []
    start = 1
    visited = []
    for i in a:
        for j in range(len(i)):
            if i[j] == 1:
                g.append(j + 1)
        k.append(g)
        g = []
    al = {id + 1: k[id] for id in range(len(k))}
    m = dfs(al, start, visited)
    # print(al)
#print(set(m))
if (count / 2 == n - 1) and len(set(m)) == n:
    print("YES")
else:
    print("NO")
