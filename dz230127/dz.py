from typing import Dict, List
from collections import deque


def dfs(al, start, visited):
    if visited is None:
        visited = set()
    visited.append(start)
    for n in al[start]:
        if not n in visited:
            dfs(al, n, visited)
    return visited
   
    
def bfs(start, finish, al):
    queue = deque([start])
    visited = {start}

    while queue:
        current = queue.popleft()
        if current == finish:
            break

        nnodes = al[current]
        for nnode in nnodes:
            if nnode not in visited:
                queue.append(nnode)
                visited[nnode] = current
    return visited


def adjency_list_from_file(filename: str):
    k = []
    g = []
    b = [[0] * len(filename) for _ in range(len(filename))]

    for i in range(len(filename)):
        b[int(filename[i][0]) - 1][int(filename[i][1]) - 1] = 1
        b[int(filename[i][1]) - 1][int(filename[i][0]) - 1] = 1

    # print(b)
    for i in b:
        for j in range(len(i)):
            if i[j] == 1:
                g.append(j + 1)
        k.append(g)
        g = []
    al = {id + 1: k[id] for id in range(len(k))}
    return al


  def main(filename: str, from_city: str, to_city: str):
        pass


# напечатать путь из города from_city до города to_city либо что его нет.

if __name__ == "__main__":
    # python main.py adjacency_list.txt москва екатеринбург
    # filename, from_city, to_city = sys.argv[1], sys.argv[2], sys.argv[3]
    # main(filename, from_city, to_city)
    visited = []
