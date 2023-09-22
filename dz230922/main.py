class Solution:
    def value_Power(n):
        count = 0
        while n!=1:
            count+=1
            if n%2==0:
                n = n//2
            else:
                n= (3*n)+1
        return count

    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {}
        for i in range(lo,hi+1):
            valpower = Solution.value_Power(i)
            dic.setdefault(i, [])
            dic[i].append(valpower)
        sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1]))
        return list(sorted_dict)[k-1]
