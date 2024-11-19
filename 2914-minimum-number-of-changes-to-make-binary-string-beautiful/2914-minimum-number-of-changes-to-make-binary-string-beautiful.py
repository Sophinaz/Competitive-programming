class Solution:
    def minChanges(self, s: str) -> int:
        result = 0
        for i in range(1, len(s)):
            if i % 2 and s[i] != s[i-1]:
                result += 1
        return result