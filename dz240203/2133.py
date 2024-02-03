class Solution:
    def checkValid(self, matrix) -> bool:
        n = len(matrix)
        for i in range(n):
            cols = set()
            rows = set()
            for j in range(n):
                if (matrix[i][j]) in cols or (matrix[j][i]) in rows:
                    return 'false'
                cols.add(matrix[i][j])
                rows.add(matrix[j][i])
        return 'true'

s = Solution()
print(s.checkValid([[1,2,3],[3,1,2],[2,3,1]]))
