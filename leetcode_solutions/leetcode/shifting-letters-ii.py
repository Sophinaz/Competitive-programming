class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        nums = [0] * n
        for a,b,c in shifts:
            if c == 0:
                nums[a] += -1
                if b  < n-1: nums[b+1] += 1
            else:
                nums[a] += 1
                if b < n-1: 
                    nums[b+1] += -1
        print(nums)
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
        print(nums)
        s = list(s)
        combine = zip(s,nums)
        result = ""
        
        for l,r in combine:
            t = (ord(l) - ord('a') + r) % 26
            
            result += chr(t + ord('a'))
        return result
                