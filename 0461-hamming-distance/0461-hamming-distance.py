class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        result = 0
        while num:
            if num & 1 == 1:
                result += 1
            num >>= 1
        return result