class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: 
            return 1 / self.myPow(x,abs(n))
        if n % 2 == 0:
            ans = self.myPow(x,n/2)
            return ans * ans
        else: 
            ans = self.myPow(x,n//2)
            return ans * ans * x


        


         