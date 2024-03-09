# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:        
        left = 0
        
        while True:
            num = (n + left) // 2
            ans = guess(num)
            
            if ans == -1:
                n = num-1
            elif ans == 1:
                left = num+1
            else: 
                return num
