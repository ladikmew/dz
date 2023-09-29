#https://leetcode.com/problems/count-all-possible-routes/description/
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        def f(start, fuel):
            if start == finish:
                count = 1
            else:
                count = 0

            for i in range(len(locations)):
                cost = abs(locations[start] - locations[i])

                if start != i and cost <= fuel:
                    count += f(i, fuel - cost)

            return count%(10 ** 9 + 7)
        return f(start, fuel)
