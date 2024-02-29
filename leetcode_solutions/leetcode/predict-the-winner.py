class Solution:

    def predictTheWinner(self, nums: List[int]) -> bool:
        def backtrack(l,r,turn,curr):
            if r == l:
                if turn %2 ==0:
                    if curr + nums[l] >= 0: return True
                    else: return False
                else:
                    if curr + nums[l] >= 0: return True
                    else: return False
                
            if turn %2 ==0:
                return backtrack(l+1,r,turn+1, curr+nums[l]) or backtrack(l,r-1,turn+1, curr+nums[r])
            else: 
                return backtrack(l+1,r,turn+1, curr-nums[l]) and backtrack(l,r-1,turn+1, curr-nums[r])
        
        return backtrack(0, len(nums)-1, 0, 0)
