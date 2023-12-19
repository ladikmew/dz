class Solution:
    def value_Power(n):
        if n==1:
            return 0
        count = 0
        if n%2==0:
            count = 1+ Solution.value_Power(n/2)
        else:
            count = 1+Solution.value_Power((3*n)+1)
        return count

    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {}
        for i in range(lo,hi+1):
            valpower = Solution.value_Power(i)
            dic.setdefault(i, [])
            dic[i].append(valpower)
        sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1]))
        return list(sorted_dict)[k-1]