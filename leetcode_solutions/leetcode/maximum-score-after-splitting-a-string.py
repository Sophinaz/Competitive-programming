class Solution:
    def maxScore(self, s: str) -> int:
        numzero,numone = 0,0
        result,left = 0,0
        for i in s:
            if i == '1': numone+=1
        
        for i in range(len(s)-1):
            if s[i] == '0': numzero += 1
            elif s[i] == '1': numone -= 1
            result = max(result, numzero + numone)
                
        return result