
n, m = map(int, input().split())
visited = []
r = []

# Создание списка смежности
graph = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v)
    graph[v - 1].append(u)
adjacency_dict = {i+1:graph[i] for i in range(len(graph))}

def dfs(al, start, visited,color):
    if visited is None:
        visited = set()
    visited.append(start)
    for n in al[start]:
        if color[n-1]!=color[start-1]:
            if color[n-1]==-1:
                color[n-1] = 1-color[start-1]
                dfs(al, n, visited,color)
        else:
            r.append(1)

def sets(n,al):
    color = [-1] * n  # Список цветов вершин (-1 - не окрашена, 0 - белая, 1 - черная)
    for i in range(n):
        if color[i]==-1:
            color[i] = 0
            f = dfs(al,i+1,visited,color)

    if len(r)>0:
        return False
    else:
        return color

s = sets(n,adjacency_dict)

l = []
if s:
    print("YES")
    for i in range(len(s)):
        if s[i]==0 or s[i]==-1:
            l.append(i+1)
    print(*l)
else:
    print("NO")
