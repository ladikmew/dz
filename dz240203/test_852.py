#должна зайти
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        return self.f(start, end, arr)

    def f(self, start, end, arr):
        id = (start + end) // 2
        if arr[id + 1] < arr[id] and arr[id - 1] < arr[id]:
            return id
        elif arr[id + 1] > arr[id] and arr[id - 1] < arr[id]:
            return self.f(id + 1, end, arr)
        elif arr[id + 1] < arr[id] and arr[id - 1] > arr[id]:
            return self.f(start, id, arr)