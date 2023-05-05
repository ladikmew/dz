n,m = list(map(int,input().split()))
a = []
for i in range(m):
    row = input().split()
    for i in range(2):
        row[i] = int(row[i])
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
    visited = []
    k = []
    g = []
    l = []
    c = 0
    t = []
    b = [[0] * n for _ in range(n)]

    for i in range(m):
        b[int(a[i][0])-1][int(a[i][1])-1] = 1
        b[int(a[i][1]) - 1][int(a[i][0]) - 1] = 1

    #print(b)
    for i in b:
        for j in range(len(i)):
            if i[j] == 1:
                g.append(j + 1)
        k.append(g)
        g = []
    al = {id + 1: k[id] for id in range(len(k))}
    print(al)
    p = dfs(al, 1, visited)
    #print(p)
    l.append(set(p))

    for i in range(1,n+1):
        visited = []
        m = dfs(al, i, visited)
        if set(m) not in l:
            l.append(set(m))
   # print(l)
print(l)
print(len(l))
for i in l:
    print(len(i))
    print(*i)




