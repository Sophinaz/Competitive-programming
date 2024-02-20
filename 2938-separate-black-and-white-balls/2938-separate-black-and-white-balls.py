class Solution:
    def minimumSteps(self, s: str) -> int:
        count = s.count('1')
        n = len(s)
        result = 0
        for i in range(n):
            if s[i] == "1":
                result += n - count - i
                count -= 1
        return result