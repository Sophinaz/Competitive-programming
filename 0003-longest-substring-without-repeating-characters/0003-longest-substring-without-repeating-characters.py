class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        left = 0
        result = 0

        for right in range(len(s)):
            if s[right] in check:
                while s[right] in check:
                    check.remove(s[left])
                    left += 1

            result = max(result, right - left + 1)
            check.add(s[right])

        return result