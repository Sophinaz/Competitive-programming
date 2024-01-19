class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        k = n
        if n %2 != 0:
            n+=1
        while True:
            if n%k==0:
                return n
            n+=2