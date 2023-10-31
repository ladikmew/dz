class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        a = [False] * n
        for par, child in edges:
            a[child] = True

        res = []
        for par in range(n):
            if not a[par]:
                res.append(par)

        return res
