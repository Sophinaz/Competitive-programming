class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        temp = set(s)
        for i in range(len(s)):
            if s[i].swapcase() not in temp:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                if len(right) > len(left): return right
                else: return left
        return s 