class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        def numtime(flips):
            res= 0
            large = 0
            for i, bit in enumerate(flips,1):
                large = max(bit,large)
                if i == large:
                    res +=1
            return res
        return numtime(flips)