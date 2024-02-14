class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        prefix = 0
        if numOnes >= k:
            return k
        else: 
            if k <= numOnes + numZeros:
                return numOnes
            else: return numOnes - (k-(numOnes + numZeros))