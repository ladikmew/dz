#должна зайти
from math import *
def diagonalPrime(self, nums: List[List[int]]) -> int:
    ans = 0
    for i in range(len(nums)):
        if self.prime(nums[i][i]):
            if nums[i][i] > ans:
                ans = nums[i][i]
        if self.prime(nums[i][len(nums) - i - 1]):
            if nums[i][len(nums) - i - 1] > ans:
                ans = nums[i][len(nums) - i - 1]
    return ans


def prime(self, num):
    for i in range(2, int(sqrt(num)) + 2):
        if (num % i == 0 and i != num) or num == 1:
            return False
    return True