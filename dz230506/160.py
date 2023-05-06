from collections import deque


def bfs(start, finish, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        current_node = queue.popleft()
        if current_node == finish:
            break

        nnodes = graph[current_node]
        for nnode in nnodes:
            if nnode not in visited:
                queue.append(nnode)
                # print(queue)
                visited[nnode] = current_node
    return visited

if __name__ == "__main__":
    g = []
    k = []
    n = int(input())
    a = []
    h = []
    r = []
    x = []
    for i in range(n):
        row = input().split()
        for i in range(len(row)):
            row[i] = int(row[i])
        a.append(row)

    s, f = list(map(int, input().split()))
    if s == f:
        print(0)
    else:
        for i in a:
            for j in range(len(i)):
                if i[j] == 1:
                    g.append(j + 1)
            k.append(g)
            g = []
        al = {id + 1: k[id] for id in range(len(k))}
        # print(al)
        m = bfs(s, f, al)
        #print(m)
        if len(m) == 1:
            print(-1)
        else:
            if f not in m.keys():
                print(-1)
            else:
                w = f
                r.append(w)
                while w != s:

                    w = m[w]
                    r.append(w)
                r = r[::-1]

                print(len(r) - 1)
                print(*r)
