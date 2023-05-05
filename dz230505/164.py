n,s = list(map(int,input().split()))
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)

def dfs(graph, start, visited):
    if visited is None:
        visited = set()
    visited.append(start)
    for n in graph[start]:
        if n not in visited:
            dfs(graph, n, visited)
    return visited



if __name__=="__main__":
    start = s
    al = {}
    g = []
    k = []
    for i in a:
        for j in range(len(i)):
            if i[j]==1:
                g.append(j+1)
        k.append(g)
        g = []
    al = {id+1: k[id] for id in range(len(k))}
    visited = []
    #print(al)
    m = dfs(al, start, visited)
#print(m)
print(len(set(m)))
