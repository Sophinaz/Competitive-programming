class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        result = []
        memo = {}

        def powerValue(n):
            if n not in memo:
                if n == 1:
                    memo[n] = 0
                    return 0

                if n % 2:
                    memo[n] = powerValue((n * 3) + 1) + 1
                else:
                    memo[n] = powerValue(n // 2) + 1
            
            return memo[n]

        for number in range(lo, hi+1):
            result.append([powerValue(number), number])
        
        result.sort()
        return result[k-1][1]