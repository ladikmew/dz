class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max = float()
        curr_max = nums[0]
        curr_min = nums[0]
        def counting_ones(n):
                w = 0
                while (n):
                    w += 1
                    n &= n - 1
                return w
        curr_bits = counting_ones(nums[0])
        for i in range(1, len(nums)):
            if counting_ones(nums[i]) != curr_bits:
                if curr_min < prev_max:
                    return False
                prev_max = curr_max
                curr_bits = counting_ones(nums[i])
                curr_max = nums[i]
                curr_min = nums[i]
            else:
                curr_max = max(curr_max, nums[i])
                curr_min = min(curr_min, nums[i])
        return curr_min >= prev_max