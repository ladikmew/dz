from typing import Dict, List
from collections import deque
def dfs(al: Dict[str, List[str]], start: str, finish: str,visited: List[str]) -> List[str]:
        if start == finish:
        return True
    if start in vizited:
        return False
    vizited += start
    for n in al[start]:
        if not n in vizited:
            if dfs(n, finish,al,vizited):
                return True
    return False
    
    
    
#     if al[start]==finish:
#         return True
#     visited.append(al[start])
#     return False
#     for i in al[start] - visited:
#         dfs(al: Dict[str, List[str]], i: str, finish: str,visited: List[str])
#     return True

#     реализация через рекурсию или стек
#     pass


def bfs(al: Dict[str, List[str]], start: str, finish: str) -> List[str]:
    squeue = deque()
    squeue+=al[start]
    vizited = []
    while squeue:
        node = squeue.popleft()
        if not node in vizited:
            if node == search:
                return True
            else:
                squeue+=graf[node]
                vizited+=[node]
    return False
    
    # реализация через очередь
    pass

    # dz_test.py
    # main.py


def main(filename: str, from_city: str, to_city: str):


# напечатать путь из города from_city до города to_city либо что его нет.

if __name__ == "__main__":
    # python main.py adjacency_list.txt москва екатеринбург
    # filename, from_city, to_city = sys.argv[1], sys.argv[2], sys.argv[3]
    # main(filename, from_city, to_city)
    visited = []
