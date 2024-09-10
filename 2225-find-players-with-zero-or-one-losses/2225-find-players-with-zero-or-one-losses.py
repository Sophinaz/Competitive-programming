class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        income = {}
        for a, b in matches:
            if b not in income:
                income[b] = 1
            else: income[b] += 1

            if a not in income:
                income[a] = 0
        result = [[] for i in range(2)]
        for i in income:
            if income[i] == 0:
                result[0].append(i)
            elif income[i] == 1:
                result[1].append(i)
        result[0].sort()
        result[1].sort()
        return result