class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m, n = len(nums), len(nums[0])
        res = 0
        for num in nums:
            num.sort()
        for i in range(n):
            max_value = 0
            for j in range(m):
                max_value = max(max_value, nums[j][i])
            res += max_value
        return res
