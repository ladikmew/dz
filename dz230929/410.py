#https://leetcode.com/problems/split-array-largest-sum/description/
import itertools


class Solution:
    def splitArray(self, nums, k) -> int:
        l = max(nums)
        r = sum(nums)
        def f(mid):
            count = 1
            cur = 0
            for i in nums:
                cur+=i
                if cur>mid:
                    count+=1
                    cur = i
                    if count>k:
                        return False
            return True

        while l<r:
            mid = (l+r)//2
            if f(mid):
                r = mid
            else:
                l = mid+1
        return  l
