class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = Counter(s1)
        l, r = 0, len(s1)
        second = Counter(s2[: len(s1)])
        while r < len(s2):
            if first == second:
                return True
            second[s2[l]] -= 1
            l += 1
            if s2[r] not in second:
                second[s2[r]] = 1
            else:
                second[s2[r]] += 1
            r+=1
        if first == Counter(s2[len(s2)-len(s1):]): 
            return True
        return False
