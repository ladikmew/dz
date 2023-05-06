from collections import dequeue

def bfs(start, finish, graph):
    queue = deque([start])
    visited = {start}

    while queue:
        current = queue.popleft()
        if current == finish:
            break

        nnodes = graph[current]
        for nnode in nnodes:
            if nnode not in visited:
                queue.append(nnode)
                visited[nnode] = current
    return visited
