class Solution:
    def minimumEffort(self, tasks) -> int:
        tasks.sort(key=lambda x: (x[1]-x[0]))
        resen = 0
        for first,second in tasks:
            resen = max(resen+first,second)
        return resen
