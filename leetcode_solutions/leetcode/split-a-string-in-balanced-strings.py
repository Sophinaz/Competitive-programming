class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left,right = 0,0
        count = 0
        result = 0

        while right < len(s):
            if s[right] == 'L': count -= 1
            else: count += 1

            if count == 0:
                result += 1
                left = right
            right += 1

        return result
