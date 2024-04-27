class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        all_in_ord = []
        count = 0
        res = 0
        k = 0
        for i in range(len(s)):
            all_in_ord.append(abs(ord(s[i]) - ord(t[i])))
        for j in range(len(s)):
            count += all_in_ord[j]
            while count > maxCost:
                count -= all_in_ord[k]
                k += 1
            res = max(res, j - k + 1)
        return res



