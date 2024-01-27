class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, r = 0, 0
        vowels = "aeiou"
        result, count = 0, 0
        while r < len(s):
            if r - l < k:
                while r - l < k:
                    if s[r] in vowels:
                        count += 1
                    r += 1
                result = max(result, count)
                continue
            result = max(result, count)
            if s[l] in vowels:
                count -= 1
            l += 1
            if s[r] in vowels:
                count += 1
                result = max(result, count)
            else:
                result = max(result, count)
            r += 1
        return result
