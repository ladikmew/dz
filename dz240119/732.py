from collections import defaultdict


class MyCalendarThree:

    def __init__(self):
        self.books = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.books[startTime] += 1
        self.books[endTime] -= 1
        res = 0
        cur = 0
        for i in sorted(self.books):
            cur += self.books[i]
            res = max(res, cur)
        return res

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(10,20)