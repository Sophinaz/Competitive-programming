class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = n // 2
        b = n // 2
        if n % 2: b += 1

        while a % 10 ==0 or b % 10 == 0:
            a -= 1
            b += 1
        return [a, b]