class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = []
        for i in range(len(scores)):
            pairs.append([scores[i], ages[i]])
        pairs.sort()
        d = []
        for i in range(len(pairs)):
            d.append(pairs[i][0])
        for i in range(len(pairs)):
            m_score, m_age = pairs[i]
            for j in range(i):
                score, age = pairs[j]
                if m_age >= age:
                    d[i] = max(d[i], m_score + d[j])
        return max(d)
