from typing import Dict, List


def dfs(al: Dict[str, List[str]], start: str, finish: str,visited: List[str]) -> List[str]:
    if al[start]==finish:
        return True
    visited.append(al[start])
    return False
    for i in al[start] - visited:
        dfs(al: Dict[str, List[str]], i: str, finish: str,visited: List[str])
    return True

    # реализация через рекурсию или стек
#     pass
#
#
# def bfs(al: Dict[str, List[str]], start: str, finish: str) -> List[str]:
#     # реализация через очередь
#     pass
#
#     # dz_test.py
#     # main.py
#
#
# def main(filename: str, from_city: str, to_city: str):
#
#
# # напечатать путь из города from_city до города to_city либо что его нет.

if __name__ == "__main__":
    # python main.py adjacency_list.txt москва екатеринбург
    # filename, from_city, to_city = sys.argv[1], sys.argv[2], sys.argv[3]
    # main(filename, from_city, to_city)
    visited = []
