class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left,right = 0,n-1
        numzero,numone = 0,0
        for i in nums:
            if i == 1: numone += 1
        maxx = numone
        result = [0]
        
        for i in range(n):
            if nums[i] == 0: numzero += 1
            else: numone -= 1

            if numzero + numone == maxx: result.append(i+1)
            elif numzero + numone > maxx:
                maxx = numzero + numone
                result = [i+1]
            
        return result

        

        
        