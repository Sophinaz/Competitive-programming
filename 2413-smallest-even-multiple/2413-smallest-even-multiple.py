class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def smallMultiple(n):
            k = n
            if n%2 != 0:
                n = n+1 
            
            while True:
                if n % k == 0:
                    return n
                n+=1
        return smallMultiple(n)
        