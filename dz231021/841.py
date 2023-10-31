class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        f = False
        def dfs(room):
            visited.add(room)
            for i in rooms[room]:
                if i not in visited:
                    dfs(i)
        dfs(0)
        if len(visited)==len(rooms):
            f = True
        return f