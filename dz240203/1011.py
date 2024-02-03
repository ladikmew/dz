class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right
        def Ship(x):
            ships, curx = 1, x
            for i in weights:
                if curx - i < 0:
                    ships += 1
                    curx = x
                curx -= i
            if ships <= days:
                return ships
        while left <= right:
            x = left + (right - left) // 2
            if Ship(x):
                res = min(x, res)
                right = x - 1
            else:
                left = x + 1
        return res